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
        #list = listhandler_local.handler.decode(str(arg))
        remote_keylist = remote_list.keys()
        local_keylist = listhandler_local.get_keys()
        #nun ausdrucken
        print(remote_keylist,local_keylist,sep="\n")

        #remote_list mit local mergen, da es sich um ein dict handelt, sind die keys unique


       # print(remote_list)

        #print(listhandler_local)

        for k in local_keylist:
            print(listhandler_local.get_entry(k))

        for k,v in remote_list.items():
           listhandler_local.add_or_override_entry(k,v)

        local_keys = listhandler_local.get_keys()
        print("sodala")
        print(local_keys)

        #ausdrucken

        #print(listhandler_local)

        #lokale liste kopieren
        #list_local = listhandler_local.copy()



