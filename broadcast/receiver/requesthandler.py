#! /usr/bin/python3

from socketserver import BaseRequestHandler

from util.config.logger import Log


class ThreadedUDPMulticastRequestHandler(BaseRequestHandler):
    """This class represents a Threaded-UDP-Multicast-Requesthandler.

    This means, that it defines methods and attributes, which will be used
    to handle a udp-multicast-request. The handle method is called by the
    super-class (BaseRequestHandler) as a new request has been received.
    """

    def __init__(self, observable_update_callback, host_ip, sender_callback, *args, **keys):
        """Shall initialize the given parameters as attributes and call the constructor of the super class.

        The observable_update_callback is in fact the update method of the observable
        implementation (in this case it may be UDPUpdateObservable). This method is called
        as a request is precessed by the handle method. As long as the received data is not
        sent by the the same host as it was received (I sent data to myself), the callback
        method is called. I define the "I sent data to myself"-thing as kickback.

        As a result of receiving lists from other hosts, the rhythm of sending our list
        to the multicast group has to be expanded. This is done by calling the sender_callback
        method. Which in fact is to expand the time of the sending rhythm.

        :param observable_update_callback: The callback of the observable implementation
        :param host_ip: The ip address of the host, where this handler is running
        :param sender_callback: The callback of the sending Thread.
        :param args: arguments for the BaseRequestHandler
        :param keys: keys for the BaseRequestHandler
        :return: None
        """
        self._observable_callback = observable_update_callback
        self._sender_callback = sender_callback

        self._own_ip = host_ip
        self._logger = Log.get_logger(self.__class__.__name__)
        BaseRequestHandler.__init__(self, *args, **keys)

    def handle(self):
        """Shall defined how to handle UDP-Multicast-Requests

        Converts the received data to a string representation.
        Checks if the received data was sent by the same host (I send data to myself),
        if this is the case, the data is dropped and a log message may be written.
        If the sender has not the same ip address as the receiver has (Another host send data to me)
        the callback method is called and the received data get processed.

        :return: None
        """
        data = str(self.request[0], "utf-8")

        if not self.is_kickback(self.client_address[0]):
            self._logger.info("received list from %s", self.client_address[0])
            self._observable_callback(data)
            self._sender_callback()

        else:
            self._logger.info("DROPPED list received from my self.")

    def is_kickback(self, client_ip):
        """Shall return if the clients ip address is equal to the attribute _own_ip


        :param client_ip: the ip of the sending client
        :return: True if the address of the sending client is equal to the receiving client.
                 False - not equal to the ip address of the sending client.
        """
        if self._own_ip == client_ip:
            return True
        return False
