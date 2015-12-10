#! /usr/bin/python3
from broadcast.manager import UDPUpdateObseravable
from util.listhandler import ListHandler


class Singleton(object):
    def __getattr__(self, item):
        return getattr(self.instance, item)

    instance = None


class UDPObservableSingleton(Singleton):
    class __Singleton(object):
        def __init__(self):
            self.observable = UDPUpdateObseravable()

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__Singleton()
        return cls.instance


class ListHandlerSingleton(Singleton):
    class __Singleton(object):
        def __init__(self):
            self.handler = ListHandler()

    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = cls.__Singleton()
        return cls.instance
