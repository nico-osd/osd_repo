#! /usr/bin/python3

from json import JSONEncoder, dumps


class ListHandler(object):
    def __init__(self):
        """
        shall construct the dict, held within this class
        """
        self._dict = {}

    def add_or_override_entry(self, ip="127.0.0.1", entry=object()):
        """
        shall add or override the key (ip) with the given value (entry).
        :param ip: the ip of the host
        :param entry: the entry for the host
        """
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
        shall return the value of the given key
        :param ip: the key
        :return: the value attached to the given key.
        """
        return self._dict.get(ip)

    def to_json(self):
        to_dump = self._dict.copy()
        return dumps(to_dump, sort_keys=True, indent=4, cls=EntryEncoder)


class Entry(object):
    def __init__(self, is_master=None, name="", pyro_uri="", last_time_active=-1):
        self._is_master = is_master
        self._name = name
        self._pyro_uri = pyro_uri
        self._last_time_active = last_time_active

    @property
    def is_master(self):
        return self._is_master

    @is_master.setter
    def is_master(self, value):
        if not self._is_master:
            self._is_master = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if value:
            self._name = value

    @property
    def pyro_uri(self):
        return self._pyro_uri

    @pyro_uri.setter
    def pyro_uri(self, value):
        if value:
            self._pyro_uri = value

    @property
    def last_time_active(self):
        return self._last_time_active

    @last_time_active.setter
    def last_time_active(self, value):
        if value:
            self._last_time_active = value


class EntryEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
