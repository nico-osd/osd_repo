import copy
import socket

class ME(object):
    def __init__(self):
        pass

    def get_ips(self, ipdict):
        """
        shall extract the keys of the given dict an return the list of key-values
        :param ipdict: the
        :return: the sorted list
        """
        key_ip_list = ipdict.keys()
        return key_ip_list

    def min_value(self, key_ip_list):
        """
        shall select the min ip within the list
        :param key_ip_list: (sorted) list of ip-addresses
        :return: min ip
        """
        min_ip = min(key_ip_list)
        return min_ip

    def update_dict(self, ipdict, min_ip):
        temp_dict = copy.deepcopy(ipdict)

# we thought about iterating over all entries to set all is_master-attributes to false, but this is not possible due to the current implementation of util.listhandler - Entry

        # Nico:
        # As soon an entry is created without explicitly passing the parameter is_master=True it is defaulted to is_master=False.
        # As long as the creator of the record (ip, entry) does not explicitly set this parameter, it wont be set anywhere.


#        for k, v in ipdict.items():
#            ipdict.get(k).is_master = False

        temp_dict.get(min_ip).is_master = True
        return temp_dict

    def am_I_master(self, ipdict):
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        return ipdict.get(ip_address).is_master

#    def sort_list(self, key_ip_list):
#        """
#        shall sort the given list according to the ip-address (ascending) and return the sorted list
#        :param key_ip_list: a list of ip-addresses that are relevant for master election
#        :return: the sorted list
#        """
#        key_ip_list.sort()
#        return key_ip_list

