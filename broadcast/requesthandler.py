#! /usr/bin/python3

from socketserver import BaseRequestHandler

from util.config.logger import Log


class ThreadedUDPMulticastRequestHandler(BaseRequestHandler):
    def __init__(self, observable_subject, *args, **keys):
        self._callback = observable_subject
        self._logger = Log.get_logger(self.__class__.__name__)
        BaseRequestHandler.__init__(self, *args, **keys)


    def handle(self):
        self._logger.info("waiting to receive msg.")
        # data = list
        data = str(self.request[0], "utf-8")

        print(data)
        # sock = self.request[1]
        # address = self.client_address[0]

        # Log.info(self, "received %s bytes from %s", len(data), str(address))
        # Log.info(self, "message: %s", data)
        # Log.info(self, "sending acknowledgement to %s", str(address))
        # sock.sendto(bytes("ack", "utf-8"), self.client_address)

        self._callback(data)
