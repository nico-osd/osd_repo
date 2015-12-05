#!/bin/python3

class IpList(object):
    def __init__(self, init=None):
        if init is not None:
            self.__dict__.update(init)


    def addItem(self,ip,name,isMaster,uri,timeStamp):
        self.__dict__.update({ip:[name,isMaster,uri,timeStamp]})

    def getList(self):
        return self

    def removeItem(self,ip):
        self.__dict__.pop(ip)



    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def __delitem__(self, key):
        del self.__dict__[key]

    def __contains__(self, key):
        return key in self.__dict__

    def __len__(self):
        return len(self.__dict__)

    def __repr__(self):
        return repr(self.__dict__)

