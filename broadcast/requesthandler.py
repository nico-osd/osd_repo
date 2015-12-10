#! /usr/bin/python3

import socketserver

from util.config.logger import Log


class ThreadedUDPMulticastRequestHandler(socketserver.BaseRequestHandler):
    def __init__(self, observable_subject, *args, **keys):
        socketserver.BaseRequestHandler.__init__(self, *args, **keys)
        self.callback = observable_subject
        self.logger = Log.get_logger(self.__class__.__name__)

    def handle(self):
        Log.info(self, "waiting to receive msg.")
        # data = list
        data = str(self.request[0], "utf-8")
        sock = self.request[1]
        address = self.client_address[0]

        Log.info(self, "received %s bytes from %s", len(data), str(address))
        Log.info(self, "message: %s", data)
        Log.info(self, "sending acknowledgement to %s", str(address))
        sock.sendto(bytes("ack", "utf-8"), self.client_address)

        self.callback(data)
