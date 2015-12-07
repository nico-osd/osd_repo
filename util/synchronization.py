#! /usr/bin/python3

"""
This is an emulation of Java's synchronized functionality,
designed by Peter Norvig.

Source: http://python-3-patterns-idioms-test.readthedocs.org/en/latest/Observer.html
"""

import threading


def synchronized(method):
    def f(*args):
        self = args[0]
        self.mutex.acquire()
        try:
            return method(*args)
        finally:
            self.mutex.release()

    return f


def synchronize(clazz, names=None):
    """Synchronize methods in the given class.
    Only synchronize the methods whose names are
    given, or all methods if names=None.
    :param clazz The class which needs synchronization
    :return: None
    """
    if isinstance(names, str):
        names = names.split()
    for (name, val) in clazz.__dict__.items():
        if callable(val) and name is not '__init__' and \
                (names is None or name in names):
            setattr(clazz, name, synchronized(val))


# You can create your own self.mutex, or inherit
# from this class:
class Synchronization:
    def __init__(self):
        self.mutex = threading.RLock()