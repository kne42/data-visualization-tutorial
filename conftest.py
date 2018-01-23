import pytest
import re
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor, CellExecutionError


class ExecutePreprocessorCell(ExecutePreprocessor):
    """ Executes individual cells in a notebook.
    """
    def preprocess(self, nb, resources={}):
        """ Preprocess notebook executing each code cell.

        The input argument `nb` is modified in-place.
        Parameters
        ----------
        nb : NotebookNode
            Notebook being executed.
        resources : dictionary
            Additional resources used in the conversion process. For example,
            passing ``{'metadata': {'path': run_path}}`` sets the
            execution path to ``run_path``. Defaults to an empty dictionary.
        """
        path = resources.get('metadata', {}).get('path', '')
        if path == '':
            path = None

        # clear display_id map
        self._display_id_map = {}

        # from jupyter_client.manager import start_new_kernel

        def start_new_kernel(startup_timeout=60, kernel_name='python', **kwargs):
            km = self.kernel_manager_class(kernel_name=kernel_name)
            km.start_kernel(**kwargs)
            kc = km.client()
            kc.start_channels()
            try:
                kc.wait_for_ready(timeout=startup_timeout)
            except RuntimeError:
                kc.stop_channels()
                km.shutdown_kernel()
                raise

            return km, kc

        kernel_name = nb.metadata.get('kernelspec', {}).get('name', 'python')
        if self.kernel_name:
            kernel_name = self.kernel_name
        self.log.info("Executing notebook with kernel: %s" % kernel_name)
        self.km, self.kc = start_new_kernel(
            startup_timeout=self.startup_timeout,
            kernel_name=kernel_name,
            extra_arguments=self.extra_arguments,
            cwd=path)
        self.kc.allow_stdin = False
        self.nb = nb
        self.resources = resources

    def cleanup(self):
        """ Cleans up the notebook kernel.

        Returns
        -------
        nb : NotebookNode
            The executed notebook.
        resources : dictionary
            Additional resources used in the conversion process.
        """
        if None in (self.kc, self.km, self.nb):
            raise AttributeError("Nothing to clean up.")
        self.kc.stop_channels()
        self.km.shutdown_kernel(now=self.shutdown_kernel == 'immediate')

        nb = self.nb
        delattr(self, 'nb')
        resources = self.resources
        delattr(self, 'resources')

        return nb, resources


def pytest_collect_file(parent, path):
    if path.ext == '.ipynb':
        return Notebook(path, parent)


class Notebook(pytest.File):
    def collect(self):
        notebook_filename = self.fspath

        with notebook_filename.open() as f:
            nb = nbformat.read(f, as_version=4)

        epc = ExecutePreprocessorCell(timeout=1000)
        def dummy(*args, **kwargs):
            # dummy function to silence log
            pass
        epc.log.debug = dummy
        epc.log.warn = dummy
        epc.log.error = dummy

        epc.preprocess(nb)
        for index, cell in enumerate(nb.cells):
            yield Cell(index, self, cell, epc)


class Cell(pytest.Item):
    def __init__(self, cell_index, parent, cell, epc):
        name = 'cell_' + str(cell_index)
        super(Cell, self).__init__(name, parent)
        self.cell = cell
        self.cell_index = cell_index
        self.epc = epc

    def runtest(self):
        self.epc.preprocess_cell(self.cell, self.epc.resources, self.cell_index)

    def repr_failure(self, excinfo):
        if excinfo.errisinstance(CellExecutionError):
            return str(excinfo.value)

    def reportinfo(self):
        return self.fspath.basename, self.cell_index, self.fspath.basename[:-6] + '::' + self.name
