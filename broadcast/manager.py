#! /usr/bin/python3

from socketserver import UDPServer
from threading import Thread, Event
from time import sleep

from broadcast.requesthandler import ThreadedUDPMulticastRequestHandler
from broadcast.sender import MulticastSender
from util.config.logger import Log
from util.config.statics import MULTICAST_GROUP
from util.patterns.observable import ObservableInterface
from util.patterns.synchronization import Synchronization, synchronize


class UDPManager(object):
    def __init__(self):
        from util.patterns.singletons import UDPObservableSingleton

        print(UDPObservableSingleton.instance.observable.update_received_list)

        #        tcpserver = TCPServer((HOST, PORT), lambda *args, **keys: SingleTCPHandler(send_server_uri, srv_uri.asString(), *args, **keys))


        self.udp_server = UDPServer(MULTICAST_GROUP, lambda *args, **keys: ThreadedUDPMulticastRequestHandler(
            UDPObservableSingleton.instance.observable.update_received_list, *args, **keys))

        self._sending_thread = UDPSenderThread()

        UDPObservableSingleton.instance.observable.set_callback(self._sending_thread.expand_timeout)

        self._receiver_thread = Thread(target=self.udp_server.serve_forever, daemon=True)

        # TODO: Testing.

    def start(self):
        if not self._receiver_thread.is_alive():
            Log.info(self, "Started UDPServer.")
            self._receiver_thread.start()

        if not self._sending_thread.is_alive():
            self._sending_thread.start()

    def stop(self):
        self.udp_server.shutdown()
        self.udp_server.server_close()
        self._sending_thread.stop()


class UDPUpdateObseravable(ObservableInterface, Synchronization):
    def __init__(self, callback=None):
        """
        shall initialize the callback to expand the timeout for sending the list.
        :param callback: the callback method to call to expand the sending rythm.
        :return: None
        """
        super().__init__()
        self.callback = callback
        self._observers = []  # list of observers
        self.logger = Log.get_logger(self.__class__.__name__)

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
        self.logger.info("registered observer %s", observer)

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

    def update_received_list(self, dct):
        self.notify_observers(dct)
        if self.callback:
            self.callback()
            self.logger.info("Callback called %s", dct)

    def set_callback(self, value):
        self.callback = value


synchronize(UDPUpdateObseravable, "add_observer remove_observer notify_observers" +
            "set_changed clear_changed has_changed update_received_list")


class UDPSenderThread(Thread):
    TIMEOUT = 2

    EXPANDED_TIMEOUT = 10

    def __init__(self):
        super().__init__()
        self.runs = Event()
        self._timeout = 2
        from util.patterns.singletons import ListHandlerSingleton
        self.singleton = ListHandlerSingleton()
        self.sender = MulticastSender()

    def run(self):
        while self.is_running():
            sleep(self.timeout)
            self.sender.send(self.singleton.handler.to_json())

    # TODO: send bye-msg, so the MC-Group is informed of this host's leaving

    def stop(self):
        self.runs.set()

    def is_running(self):
        return self.runs.is_set()

    @property
    def timeout(self):
        return self._timeout

    def expand_timeout(self):
        if self.timeout == self.TIMEOUT:
            self._timeout = self.EXPANDED_TIMEOUT
