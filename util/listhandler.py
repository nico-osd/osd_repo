#! /usr/bin/python3

from copy import deepcopy, copy
from json import JSONEncoder, dumps

from util.synchronization import Synchronization, synchronize


class ListHandler(Synchronization):
    def __init__(self):
        """
        shall construct the dict, held within this class
        """
        super().__init__()
        self._dict = {}

    def add_or_override_entry(self, ip="127.0.0.1", entry=None):
        """
        shall add or override the key (ip) with the given value (entry).
        :param ip: the ip of the host
        :param entry: the entry for the host
        """
        print(entry, ip)

        if isinstance(entry, Entry):
            self._dict[ip] = entry
        else:
            raise TypeError

    def rmv_entry(self, ip):
        """
        shall remove a given entry and return the value which was attached to it.
        :param ip: the key of the key-value pair to remove
        :return: the value which was attached to the key
        """
        return self._dict.pop(ip)

    def get_entry(self, ip):
        """
        shall return a deepcopy of the value of the given key
        :param ip: the key
        :return: the value attached to the given key.
        """
        return deepcopy(self._dict.get(ip))

    def get_keys(self):
        """
        shall return a copy of the keys of the held dict.
        :return: copy the keys held within the dict
        """
        return copy(self._dict.keys())

    def to_json(self):
        to_dump = self._dict.copy()
        return dumps(to_dump, sort_keys=True, indent=4, cls=EntryEncoder)


synchronize(ListHandler, "add_or_override_entry rmv_entry get_entry to_json")


class Entry(object):
    def __init__(self, is_master=False, name="", pyro_uri="", last_time_active=-1):
        self._is_master = is_master
        self._name = name
        self._pyro_uri = pyro_uri
        self._last_time_active = last_time_active

    @property
    def is_master(self):
        return copy(self._is_master)

    @is_master.setter
    def is_master(self, value):
        if not self._is_master:
            self._is_master = value

    @property
    def name(self):
        return copy(self._name)

    @name.setter
    def name(self, value):
        if value:
            self._name = value

    @property
    def pyro_uri(self):
        return copy(self._pyro_uri)

    @pyro_uri.setter
    def pyro_uri(self, value):
        if value:
            self._pyro_uri = value

    @property
    def last_time_active(self):
        return copy(self._last_time_active)

    @last_time_active.setter
    def last_time_active(self, value):
        if value:
            self._last_time_active = value

    @staticmethod
    def as_entry(dct):
        pass


class EntryEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__