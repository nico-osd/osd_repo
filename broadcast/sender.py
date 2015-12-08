#! /usr/bin/python3

import socket
import struct
from threading import Thread, Event

from broadcast.manager import MULTICAST_GROUP
from util.logger import Log


class MulticastSender(Thread):
    def __init__(self, to_send=""):
        super().__init__()
        if to_send == "":
            return

        self.logger = Log.get_logger(self.__class__.__name__)

        self.to_send = to_send

        self.is_running = Event()

        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.timeout(1)
        ttl = struct.pack("b", 1)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    def run(self):
        if self.to_send == "":
            return

        self.sock.sendto(bytes(self.to_send, "utf-8"), MULTICAST_GROUP)

        while self.runs():
            self.logger.info("waiting to receive")
            try:
                data, server = self.sock.recvfrom(16)
            except socket.timeout:
                self.logger.debug("timed out, no responses")
                return
            self.logger.info("received %s from %s ", data, server)

    def runs(self):
        return self.is_running.is_set()

    def stop(self):
        self.is_running.set()
