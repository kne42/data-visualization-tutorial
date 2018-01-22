from __future__ import print_function
from inspect import getsourcelines as source


class Solutions:
    """ A collection of solutions.
    """
    def __init__(self):
        pass

    def add(self, func):
        """ Decorator for problem solutions.
        """
        source_code = source(func)

        def placeholder():
            print(''.join(source_code[0][1:]))
            func()

        setattr(self, func.__name__, placeholder)
