#!/usr/bin/env python
from abc import ABCMeta, abstractmethod


class ObserverInterface(metaclass=ABCMeta):
    """Observer pattern: Observer interface"""

    @abstractmethod
    def update(self, observable, arg):
        pass
