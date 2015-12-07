
from util.listhandler import Entry

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

#    def sort_list(self, key_ip_list):
#        """
#        shall sort the given list according to the ip-address (ascending) and return the sorted list
#        :param key_ip_list: a list of ip-addresses that are relevant for master election
#        :return: the sorted list
#        """
#        key_ip_list.sort()
#        return key_ip_list

    def min_value(self, key_ip_list):
        """
        shall select the min ip within the list
        :param key_ip_list: (sorted) list of ip-addresses
        :return: min ip
        """

        min_ip = min(key_ip_list)

        return min_ip

    def update_dict_entry(self, ):
        pass

#class CallME:
#    ME.min_value(x)

#if __name__ == "__main__";
#    CallME.min(x)
