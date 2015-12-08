#!/usr/bin/env python

"""Observer pattern:

Observer defines a one-to-many dependency between objects
so that when one object changes state, all its dependents
are notified and updated automatically.

Provides an observable main class that notifies observers
or listener of changes happening in the observed class.
"""
from abc import ABCMeta, abstractmethod

from util.logger import get_logger
from util.synchronization import synchronize, Synchronization


class ObservableInterface(metaclass=ABCMeta):
    """Observer pattern: Observable interface"""

    def __init__(self):
        super().__init__()
        self._changed = False  # Flag indicating changes

    @abstractmethod
    def add_observer(self, observer): pass

    @abstractmethod
    def remove_observer(self, observer): pass

    @abstractmethod
    def notify_observers(self, arg): pass

    def set_changed(self): self._changed = True

    def clear_changed(self): self._changed = False

    def has_changed(self): return self._changed


# end class

import random  # required to update _privateData


class ObservableImplementation(ObservableInterface, Synchronization):
    """Observer pattern: Implementation class for Observable"""

    def __init__(self):
        super().__init__()
        self._observers = []  # list of observers
        self.logger = get_logger(self.__class__.__name__)

    def add_observer(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
        self.logger.debug("registered observer %s", observer)

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

    def update_private_data(self):
        private_data = random.randint(0, 10)
        self.notify_observers(private_data)


synchronize(ObservableImplementation, "add_observer remove_observer notify_observers" +
            "set_changed clear_changed has_changed")


# end class

class ObserverInterface(metaclass=ABCMeta):
    """Observer pattern: Observer interface"""

    @abstractmethod
    def update(self, observable, arg):
        pass


# end class

class Observer(ObserverInterface):
    """Observer pattern: Implementation class for Observer"""

    _observed = ''

    def __init__(self, observed=''):
        super().__init__()
        self._observed = observed
        self.logger = get_logger(self.__class__.__name__)

    def subscribe_observed(self, observed):
        observed.add_observer(self)

    def unsubscribe_observed(self, observed):
        observed.remove_observer(self)

    def update(self, observable, arg):
        # TODO: implement update function
        self.logger.debug("Me: %s Data: %s", self, arg)


# end class

if __name__ == '__main__':
    subject = ObservableImplementation()
    obs1 = Observer()
    obs2 = Observer()
    subject.add_observer(obs1)
    subject.update_private_data()
    subject.add_observer(obs2)
    subject.update_private_data()
    subject.remove_observer(obs1)
    subject.update_private_data()
