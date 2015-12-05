#!/bin/python3

#! /usr/bin/python3

from json import JSONEncoder


class ListHandler(object):
    def __init__(self):
        """
        shall constructs the dict, held within this class
        """
        self._dict = {}

    def add_or_override_entry(self, ip="127.0.0.1", entry=object()):
        """
        shall add or override the key (ip) with the given value (entry).
        :param ip: the ip of the host
        :param entry: the entry for the host
        """
        self._dict[ip] = entry

    def rmv_entry(self, ip):
        """
        shall remove a given entry and return the value which was attached to it.
        :param ip: the key of the key-value pair to remove
        :return: the value which was attached to the key
        """
        return self._dict.pop(ip)

    def get_entry(self, ip):
        """
        shall return the value of the given key
        :param ip: the key
        :return: the value attached to the given key.
        """
        return self._dict.get(ip)

    def get_dict(self):
        """
        this method will be removed as it is only for testing.
        :return: dict.
        """
        return self._dict


class Entry(object):
    def __init__(self, isMaster=None, name="", pyro_uri="", timestamp=-1):
        self._isMaster = isMaster
        self._name = name
        self._pyro_uri = pyro_uri
        self._last_time_active = timestamp

    def set_is_master(self, isMaster=False):
        if not self._isMaster:
            self._isMaster = isMaster

    def set_name(self, name=""):
        if not self._name:
            self._name = name

    def set_pyro_uri(self, pyro_uri=""):
        if not self._pyro_uri:
            self._pyro_uri = pyro_uri

    def set_last_time_active(self, timestamp=-1):
        self._last_time_active = timestamp

    def get_is_master(self):
        return self._isMaster

    def get_name(self):
        return self._name

    def get_pyro_uri(self):
        return self._pyro_uri

    def get_last_time_active(self):
        return self._last_time_active


class EntryEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__