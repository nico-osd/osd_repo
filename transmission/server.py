#! /usr/bin/python3
from __future__ import print_function
import time
from transmission.action import Action


class Server(object):
    def __init__(self):
        self._registered_names = []

    def register_name(self, nico):
        self._save_action(nico, "REGISTER")

    def deregister_name(self, name):
        self._save_action(name, "DE-REGISTER")

    def _save_action(self, name, action):
        cur_time = int(time.time())
        temp_name = Action(name, cur_time, action)
        self._registered_names.append(temp_name)

        # Print some info
        print("[" + cur_time + "]: Client\"" + name + "\" did: [", action, "]")
