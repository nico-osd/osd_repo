#! /usr/bin/python3
from __future__ import print_function
import Pyro4


class Client(object):
    def __init__(self, name):
        self._name = name
        self._server = object()

    def connect(self, host="10.20.0.100", port=9090):
        # locating, throws an exception if there is no NameServer
        ns = Pyro4.locateNS(host, port)
        # connecting
        self._server = Pyro4.Proxy("PYRONAME:transmission.server")

    def register(self):
        self._server.register_name(self._name)

    def deregister(self):
        self._server.deregister_name(self._name)
