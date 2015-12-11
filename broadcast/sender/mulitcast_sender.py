#! /usr/bin/python3

import socket
import struct

from util.config.statics import MULTICAST_GROUP


class MulticastSender(object):
    """An instance of this class shall send a package to the multicast group.
    """

    @staticmethod
    def send(to_send=""):
        """Shall send the given string to_send to the multicast group.

        As this is UDP-based it is a fire-and-forget circle. We do not
        know if the package was successfully sent or received and in the
        end we do not care about it. As this method is called regularly
        it is not important at all if one package is not successfully
        transmitted.

        :param to_send: a string which shall be send to the multicast group
        :return: None
        """

        # if there is nothing to send, we do not need to do anything.
        if to_send == "":
            return
        # create socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # set ttl passed as struct to the setsockopt method.
        ttl = struct.pack("b", 1)
        sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

        # send to_send to multicast group
        sock.sendto(bytes(to_send, "utf-8"), MULTICAST_GROUP)

        # finally close the socket.
        sock.close()
