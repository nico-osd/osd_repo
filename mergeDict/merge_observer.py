#! /usr/bin/python3
from util.config.logger import Log
from util.patterns.observer.observer import ObserverInterface
from util.patterns.singletons import ListHandlerSingleton


class MergeObserver(ObserverInterface):
    """Observer pattern: Implementation class for Observer"""

    def __init__(self, observed=''):
        super().__init__()
        self.list = []

    def subscribe_observed(self, observed):
        observed.add_observer(self)

    def unsubscribe_observed(self, observed):
        observed.remove_observer(self)

    def update(self, observable, arg):
        self.list.append(arg)
        # TODO: implement update function

        listhandler = ListHandlerSingleton.instance
        list = listhandler.handler.decode(str(arg))
        Log.info(self, "Data: %s", str(arg))
        Log.info(self, "Interpreted: %s", str(list))
