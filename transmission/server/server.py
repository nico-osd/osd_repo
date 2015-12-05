#! /usr/bin/python3
from __future__ import print_function
import time
import Pyro4
from socketserver import BaseRequestHandler
from transmission.server.action import Action


class Server(object):
    def __init__(self):
        self._registered_names = []

    @Pyro4.oneway
    def register_name(self, name):
        self._save_action(name, "REGISTER")

    @Pyro4.oneway
    def deregister_name(self, name):
        self._save_action(name, "DE-REGISTER")

    def _save_action(self, name, action):
        cur_time = int(time.time())
        temp_name = Action(name, cur_time, action)
        self._registered_names.append(temp_name)

        # Print some info
        print("[" + str(cur_time) + "]: Client \"" + name + "\" did: [", action, "]")


class SingleTCPHandler(BaseRequestHandler):
    def __init__(self, callback, srv_uri, *args, **keys):
        self.callback = callback
        self.srv_uri = srv_uri
        BaseRequestHandler.__init__(self, *args, **keys)

    def handle(self):
        self.data = str(self.request.recv(1024), "utf-8")
        self.callback(self.data, self.srv_uri)


def send_server_uri(client_uri, srv_uri):
    client = Pyro4.Proxy(client_uri)
    client.master_uri(srv_uri)
