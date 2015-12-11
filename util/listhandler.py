#! /usr/bin/python3

from copy import deepcopy, copy
from json import JSONEncoder, dumps, JSONDecoder

from util.patterns.synchronization import Synchronization, synchronize


class ListHandler(Synchronization):
    def __init__(self):
        """Shall construct the dict, held within this class
        """
        super().__init__()
        self._dict = {}

    def add_or_override_entry(self, ip="127.0.0.1", entry=None):
        """Shall add or override the key (ip) with the given value (entry).


        :param ip: the ip of the host
        :param entry: the entry for the host
        """
        if isinstance(entry, Entry):
            self._dict[ip] = entry
        else:
            raise TypeError

    def rmv_entry(self, ip):
        """Shall remove a given entry and return the value which was attached to it.


        :param ip: the key of the key-value pair to remove
        :return: the value which was attached to the key
        """
        return self._dict.pop(ip)

    def get_entry(self, ip):
        """Shall return a deepcopy of the value of the given key


        :param ip: the key
        :return: the value attached to the given key.
        """
        return deepcopy(self._dict.get(ip))

    def get_keys(self):
        """Shall return a copy of the keys of the held dict.


        :return: copy the keys held within the dict
        """
        return self._dict.keys()

    def to_json(self):
        """Shall convert _dict attribute to json format and return it


        :return: the json representation of the _dict attribute
        """
        to_dump = self._dict.copy()
        return dumps(to_dump, sort_keys=True, indent=4, cls=EntryEncoder)

    @staticmethod
    def decode(json_str):
        """Shall decode the given json representation to python dict.


        :param json_str: the json representation of the dict.
        :return: a python representation of the given json string
        """
        dct = JSONDecoder().decode(json_str)
        # target format: { '10.20.0.123' : Entry(...), ... }
        target = {}
        for k in iter(dct):
            target[k] = Entry.as_entry(dct[k])
        return target

    def __str__(self):
        """Shall return a string representation of the _dict attribute.


        :return: string representation of the _dict attribute.
        """
        rtn = ''

        cpy_dict = self._dict.copy()

        for k in iter(cpy_dict):
            rtn = (rtn + "{0}:\n {1}").format(k, str(cpy_dict[k]))
        return rtn


synchronize(ListHandler, "add_or_override_entry rmv_entry get_entry to_json decode")


class Entry(object):
    """This class holds the attributes of a host within the network.
    """

    def __init__(self, is_master=False, pyro_uri="", last_time_active=-1):
        """Shall initialize the attributes with the given (default-) parameters.


        :param is_master: defines if is this entry a master node
        :param pyro_uri: the pyro uri of this entry
        :param last_time_active: the timestamp of the last activity received from the remote host.
        :return: None
        """
        self._is_master = is_master
        self._pyro_uri = pyro_uri
        self._last_time_active = last_time_active

    @property
    def is_master(self):
        """Shall return a copy of the is_master attribute


        :return: True if this Entry is master
                 False if not.
        """
        return copy(self._is_master)

    @is_master.setter
    def is_master(self, value):
        """Shall set the is_master value if it is not already set.


        :param value: True or False - True if and only if this is the master Entry.
        :return: None
        """
        if not self._is_master:
            self._is_master = value

    @property
    def pyro_uri(self):
        """Shall return the Pyro_uri attribute of this entry.


        :return: a copy of the pyro uri of this entry.
        """
        return copy(self._pyro_uri)

    @pyro_uri.setter
    def pyro_uri(self, value):
        """Shall set the pyro_uri attribute, if value is defined.


        :param value: The pyro_uri to set.
        :return: None
        """
        if value:
            self._pyro_uri = value

    @property
    def last_time_active(self):
        """Shall return a copy of the attribute last_time_active.

        The attribute is a timestamp following the POSIX standard.

        :return: a copy of the last_time_active attribute
        """
        return copy(self._last_time_active)

    @last_time_active.setter
    def last_time_active(self, value):
        """Shall set the last_time_active attribute to the given value

        Shall only set the attribute if the given value is defined (not None)

        :param value: the value to set.
        :return: None
        """
        if value:
            self._last_time_active = value

    def __str__(self):
        """ Shall return the string representation of the object.


        :return: string representation of this object.
        """
        rtn = ''
        for k in iter(self.__dict__):
            rtn = (rtn + "\t[{0}]: {1}\n").format(k, self.__dict__[k])
        return rtn

    @staticmethod
    def as_entry(dct):
        """Shall construct a new Entry object with the given dict.

         This does only work if the given dct hast the following arguments defined:

         dct['_is_master'], dct['_pyro_uri'], dct['_last_time_active']

        :param dct: a dictionary representation of the attributed held by this class.
        :return: A new entry object with the given values as attributes.
        """
        return Entry(dct['_is_master'], dct['_pyro_uri'], dct['_last_time_active'])


class EntryEncoder(JSONEncoder):
    """This class represents the rules, how an Entry is encoded to json format.
    """
    def default(self, o):
        """Shall return the attributes from the given object which shall be converted to json.


        :param o: an (Entry-) object
        :return: json representation of the given object.
        """
        return o.__dict__
