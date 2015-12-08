#! /usr/bin/python3

from socketserver import UDPServer
from threading import Thread

from broadcast.requesthandler import ThreadedUDPMulticastRequestHandler
from util.logger import Log
from util.observable import ObservableInterface
from util.synchronization import Synchronization, synchronize

MULTICAST_GROUP = ("224.0.0.1", 10000)


class UDPManager(object):
    def __init__(self):
        self.observable = UDPUpdateObseravable()
        self.udp_server = UDPServer(MULTICAST_GROUP,
                                    lambda *args, **keys: ThreadedUDPMulticastRequestHandler(
                                        self.observable.update_received_list,
                                        *args, **keys))

        self._receiver_thread = Thread(target=self.udp_server, daemon=True)

        def start(self):
            if not self._receiver_thread.is_alive():
                Log.info("Started UDPServer.")
                self._receiver_thread.start()


class UDPUpdateObseravable(ObservableInterface, Synchronization):
    def __init__(self):
        super().__init__()
        self._observers = []  # list of observers

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
        Log.info("registered observer %s", observer)

    def remove_observer(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, arg):

        with self.mutex:
            if self.has_changed():
                return

            tmp_copy = self._observers.copy()

            self.clear_changed()

        for x in tmp_copy:
            x.update(self, arg)

    def update_received_list(self, ip, list):
        self.notify_observers(list)


synchronize(UDPUpdateObseravable, "add_observer remove_observer notify_observers" +
            "set_changed clear_changed has_changed")
