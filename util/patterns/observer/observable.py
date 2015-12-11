#! /usr/bin/python3
from abc import abstractmethod, ABCMeta


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
