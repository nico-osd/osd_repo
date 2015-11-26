#! /usr/bin/python3


class Action(object):
    def __init__(self, name, timestamp, action):
        self._action = action
        self._name = name
        self._timestamp = timestamp

    def name(self):
        return self._name

    def timestamp(self):
        return self._timestamp

    def action(self):
        return self._action

