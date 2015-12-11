#! /usr/bin/python3

from socketserver import UDPServer
from threading import Thread

from broadcast.receiver.requesthandler import ThreadedUDPMulticastRequestHandler
from broadcast.receiver.udp_observable import UDPUpdateObseravable
from broadcast.sender.sender_thread import UDPSenderThread
from util.config.logger import Log
from util.config.statics import MULTICAST_GROUP
from util.patterns.singletons import UDPObservableSingleton
from util.patterns.synchronization import synchronize


class UDPManager(object):
    """This class starts and stops the sending and receiving threads.
    """

    def __init__(self, host_ip):
        """Initializes the attributes

        :param host_ip: The ip of the network interface where this service is running.
        :return: None
        """

        # initializes the Sender Thread
        self._sending_thread = UDPSenderThread()

        # initializes the udpserver with our ThreadedUDPMulticastRequestHandler

        # as arguments for the constructor of the RequestHandler we have to pass
        # the update method of the Observable Implementation and the ip-address of the network interface
        # where this service is running.
        self.udp_server = UDPServer(MULTICAST_GROUP, lambda *args, **keys: ThreadedUDPMulticastRequestHandler(
            UDPObservableSingleton.instance.observable.update_received_list,
            host_ip, self._sending_thread.expand_timeout, *args, **keys))

        self._receiver_thread = Thread(target=self.udp_server.serve_forever, daemon=True)

        self._logger = Log.get_logger(self.__class__.__name__)

    def start(self):
        if not self._sending_thread.is_alive():
            self._logger.info("Started SenderThread.")
            self._sending_thread.start()

        if not self._receiver_thread.is_alive():
            self._logger.info("Started UDPServer.")
            self._receiver_thread.start()

    def stop(self):
        if self._sending_thread.is_alive():
            self._logger.info("Stopping SenderThread...")
            self._sending_thread.stop()

        if self._receiver_thread.is_alive():
            self._logger.info("Stopping UDPServer...")
            self.udp_server.shutdown()
            self.udp_server.server_close()


synchronize(UDPUpdateObseravable, "add_observer remove_observer notify_observers" +
            "set_changed clear_changed has_changed update_received_list")