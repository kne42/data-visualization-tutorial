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
    res = call('tests/solution_example.py')
    assert res == ['#!/usr/bin/env solutions',
                   '',
                   '"""Hello World!"""',
                   '']


def test_output():
    res = call('tests/solution_print.py')
    assert res == ['#!/usr/bin/env solutions',
                   '',
                   'print("""Hello World!""")',
                   'Hello World!',
                   '']
