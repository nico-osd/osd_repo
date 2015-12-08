#!/bin/python3

import time


class TwoDicts(object):
    def __init__(self,dict1,dict2):
        self._dict = {}


    def compareDict(self, dict1, dict2):
        pass

    def getMergedDict(self,dict1,dict2):
        dict3 = dict1.copy()  #kopie von liste1 erstellen
        dict3.update(dict2) #liste2 dazu mergen
        dict4 = dict3.copy() #wird zur ausgabeliste
        ts = time.time() #aktuellen timestamp generieren
        for k,v in dict3.items():
           # delta = referendeTime - savedTime
            delta = ts - v[3]
            print(delta)
            if delta > 300:
                print(k,v)
                print(type(k))
                dict4.pop(k)

        return dict4

