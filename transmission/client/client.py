#! /usr/bin/python3
from __future__ import print_function
import Pyro4
from threading import Thread, Event
import socket
import time


class Client(Thread):
    def __init__(self, name, host, *args, **kwargs):
        Thread.__init__(self, *args, **kwargs)
        self._server = object()
        self._daemon = Pyro4.Daemon(host=Pyro4.socketutil.getInterfaceAddress(host))
        self._contact = FirstContact(self.stop)
        self.uri = self._daemon.register(self._contact)
        self.event = Event()
        self.srv_uri = None

    def get_uri(self):
        return self.uri

    def run(self):
        self._daemon.requestLoop(loopCondition=self.is_running)

    def stop(self, srv_uri):
        self.event.set()
        self.srv_uri = srv_uri
        self._release_thread()

    def get_srv_uri(self):
        return self.srv_uri

    def is_running(self):
        return not self.event.is_set()

    def _release_thread(self):
        client = Pyro4.Proxy(self.uri)
        client.release_thread()


class FirstContact(object):
    def __init__(self, callback):
        self._callback = callback

    @Pyro4.oneway
    def master_uri(self, srv_uri):
        self._callback(srv_uri)

    @Pyro4.oneway
    def release_thread(self):
        pass


class Contact(object):
    def __init__(self, name, srv_uri):
        self._srv_uri = srv_uri
        self._server = None
        self._name = name

    def register(self):
        if self._server is None:
            self._server = Pyro4.Proxy(self._srv_uri)
        self._server.register_name(self._name)

    def deregister(self):
        self._server.deregister_name(self._name)


class TCPSender(object):
    @staticmethod
    def send(data, host_port=("localhost", 9999)):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            sock.connect(host_port)
            sock.sendall(bytes(data, "utf-8"))
        finally:
            sock.close()
