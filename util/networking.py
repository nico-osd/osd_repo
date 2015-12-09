#! /usr/bin/python3

"""
From: http://code.activestate.com/recipes/439094-get-the-ip-address-associated-with-a-network-inter/

Implements a function, which returns the ip-address assigned to the network interface identified by the name given.
"""

import fcntl
import socket
import struct


def get_ip_address(ifname):
    """
    shall return the ip address of the given interface-name
    :param ifname: the name of the network interface
    :return: ip address assigned to the network interface
    """
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack(b'256s', bytes(ifname[:15], "utf-8"))
    )[20:24])

    # usage:
    # get_ip_address('lo')
    # returns: '127.0.0.1'
    # get_ip_address('eth0')
    # returns: '38.113.228.130'
