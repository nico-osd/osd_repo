#! /usr/bin/python3
from util.config.logger import Log
from util.patterns.observer.observable import ObservableInterface
from util.patterns.synchronization import Synchronization


class UDPUpdateObseravable(ObservableInterface, Synchronization):
    def __init__(self):
        """Shall initialize the list and a logger.

        :return: None
        """
        super().__init__()
        self._observers = []  # list of observers
        self.logger = Log.get_logger(self.__class__.__name__)

    def add_observer(self, observer):
        """Shall add given observer to the list of observers, if it has not already been added.


        :param observer: the observer object to add
        :return: None
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def remove_observer(self, observer):
        """Shall remove the given observer from list of observers, if it has already been added.


        :param observer:
        :return: None
        """
        if observer in self._observers:
            self._observers.remove(observer)

    def notify_observers(self, arg):
        """Shall notify observers, while doing that the self.object is locked.


        :param arg: the parameter to pass to the update method implemented by the observers.
        :return: None
        """
        with self.mutex:
            if self.has_changed():
                return

            tmp_copy = self._observers.copy()

            self.clear_changed()

        for x in tmp_copy:
            x.update(self, arg)

    def update_received_list(self, arg):
        """Shall call notify_observers to notify registered observers.


        :param arg: The argument which shall be passed to the observers update method.
        :return: None
        """
        self.notify_observers(arg)
