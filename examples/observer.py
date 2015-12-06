#!/usr/bin/env python

'''Observer pattern:

Observer defines a one-to-many dependency between objects
so that when one object changes state, all its dependents
are notified and updated automatically.

Provides an observable main class that notifies observers
or listener of changes happening in the observed class.
'''

class ObservableInterface():
    '''Observer pattern: Observable interface'''
    
    def __init__(self):
        pass;
    
    def addObserver(self, observer):
        pass;
    
    def removeObserver(self, observer):
        pass;
    
    def notifyObservers(self):
        pass;
#end class

import random;                  # required to update _privateData

class ObservableImplementation(ObservableInterface):
    '''Observer pattern: Implementation class for Observable'''
    
    _observers = [];            # list of observers
    _privateData = 1;           # private data
    
    def __init__(self):
        _observers = [];
    
    def addObserver(self, observer):
        self._observers.append(observer);
        print ("registered observer %s", observer)
    
    def removeObserver(self, observer):
        self._observers.remove(observer);
    
    def notifyObservers(self):
        for x in self._observers:
            x.update(self._privateData);
    
    def updatePrivateData(self):
        _privateData = random.randint(0, 10);
        self.notifyObservers();
#end class

class ObserverInterface():
    '''Observer pattern: Observer interface'''
    
    def __init__(self):
        pass;
    
    def update(self):
        pass;
#end class

class Observer(ObserverInterface):
    '''Observer pattern: Implementation class for Observer'''
    
    _observed = '';
    
    def __init__(self, observed = ''):
        self._observed = observed;
        print(self);
    
    def subscribeObserved(self, observed):
        observed.addObserver(self);
    
    def unsubscribeObserved(self, observed):
        observed.removeObserver(self);
    
    def update(self, data):
        # TODO: implement update function
        print("Me: ", self, " Data: ", data);
#end class

if (__name__ == '__main__'):
    subject = ObservableImplementation();
    obs1 = Observer();
    obs2 = Observer();
    subject.addObserver(obs1);
    subject.updatePrivateData();
    subject.addObserver(obs2);
    subject.updatePrivateData();
    subject.removeObserver(obs1);
    subject.updatePrivateData();
