#! /usr/bin/python3

import socket
import struct

from util.config.logger import Log
from util.config.statics import MULTICAST_GROUP


class MulticastSender(object):
    def __init__(self):
        self.logger = Log.get_logger(self.__class__.__name__)

    def send(self, to_send=""):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        ttl = struct.pack("b", 1)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

        if to_send == "":
            return
        self.sock.sendto(bytes(to_send, "utf-8"), MULTICAST_GROUP)

        self.sock.shutdown()
        self.sock.close()
