#!/usr/bin/env python

from __future__ import print_function
import sys
import os
import re

from IPython.display import Markdown


if len(sys.argv) != 2:
    print("Usage: hidden.py dirname")
    sys.exit(-1)

dirname = sys.argv[1]
if dirname[-1] != '/':
    dirname += '/'


def _show(path):
    """ Converts a markdown file to something readable by IPython.

    Parameters
    ----------
    filename : str
        The file's path.

    Returns
    -------
    markdown : IPython.core.display.Markdown
    """
    with open(path, 'r') as f:
        content = f.read()

    return Markdown(content)


class Lesson:
    """ Loads a directory's Markdown files and renders them as objects usable by IPython.

    Parameters
    ----------
    path : str
        The directory's path.
    """
    def __init__(self, path):
        files = os.listdir()
        for f in files:
            if re.search(r'^.*\.md$', f):
                setattr(self, f[:-3], _show(path + f))


section = Lesson(dirname)
