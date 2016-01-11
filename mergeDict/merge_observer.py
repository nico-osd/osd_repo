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
        #print(listhandler)
        list = listhandler.handler.decode(str(arg))
        print(list)
        Log.info(self, "Data: %s", str(arg))
        Log.info(self, "Interpreted: %s", str(list))
        self.merge(list)

    def merge(self,remote_list):
        #print(remote_list)
        listhandler_local = ListHandlerSingleton.instance.handler
        remote_keylist = remote_list.keys()
        local_keylist = listhandler_local.get_keys()
        #nun ausdrucken
        print(remote_keylist,local_keylist,sep="\n")

        #remote_list mit local mergen, da es sich um ein dict handelt, sind die keys unique

        for k,v in remote_list.items():
            print(k,v)

        for k,v in listhandler_local.items():
            print(k,v)


        print(listhandler_local)
        #print(remote_list)

        listhandler_local.update(remote_list)

        #ausdrucken

        #print(listhandler_local)

        #lokale liste kopieren
        #list_local = listhandler_local.copy()



