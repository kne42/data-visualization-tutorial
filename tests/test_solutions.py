import shlex
import subprocess


def call(cmd):
    """Runs a bash command.

    Parameters
    ----------
    cmd : String
        The command to run.

    Returns
    -------
    result : [List of String]
        The output of the command."""
    return subprocess.check_output(shlex.split(cmd),
                                   universal_newlines=True).split('\n')


def test_read():
    res = call('sol.py tests/solution_example.py')
    assert '"""Hello World!"""' in res


def test_output():
    res = call('sol.py tests/solution_print.py')
    assert 'print("""Hello World!""")' in res and 'Hello World!' in res
