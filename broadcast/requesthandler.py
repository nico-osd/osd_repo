#! /usr/bin/python3

import socketserver

from util.logger import Log


class ThreadedUDPMulticastRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, observable_subject, *args, **keys):
        socketserver.BaseRequestHandler.__init__(self, *args, **keys)
        self.callback = observable_subject
        self.logger = Log.get_logger(self.__class__.__name__)

    def handle(self):
        self.logger.info("waiting to receive msg.")
        # data = list
        data = str(self.request[0], "utf-8")
        sock = self.request[1]
        address = self.client_address[0]

        self.logger.info("received %s bytes from %s", len(data), str(address))
        self.logger.info("message: %s", data)
        self.logger.info("sending acknowledgement to %s", str(address))
        sock.sendto(bytes("ack", "utf-8"), self.client_address)

        self.callback(data)
