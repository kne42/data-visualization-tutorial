# credit: https://github.com/ghego/travis_anaconda_jupyter

import subprocess


def _exec_notebook(path):
    args = ["jupyter", "nbconvert", "--to", "notebook", "--execute",
            "--ExecutePreprocessor.timeout=1000",
            "--output", path, path]
    subprocess.check_call(args)


def test():
    _exec_notebook('01-intro-to-jupyter.ipynb')
