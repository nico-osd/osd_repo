#!/bin/python3

from mergeDict.listHandler import ListHandler, Entry
from mergeDict.compareDict import TwoDicts
import time
import datetime

list1 = ListHandler()
list2 = ListHandler()

# create Entries

list1.add_or_override_entry('10.20.0.200',entry=['FALSE','raspi_aaa','pyrouri',time.time()])
list1.add_or_override_entry('10.20.0.199',entry=['FALSE','raspi_bbb','pyrouri',time.time()-150])
list1.add_or_override_entry('10.20.0.19',entry=['FALSE','raspi_ccc','pyrouri',time.time()-250])

list2.add_or_override_entry('10.20.0.200',entry=['FALSE','raspi_ddd','pyrouri',time.time()])
list2.add_or_override_entry('10.20.0.23',entry=['FALSE','raspi_eee','pyrouri',time.time()-350])
list2.add_or_override_entry('10.20.0.1',entry=['FALSE','raspi_fff','pyrouri',time.time()-270])

# create temporary dicts from list handlers

temp1 = list1.get_dict()
temp2 = list2.get_dict()

#print(type(temp1))

# merge dicts

temp = TwoDicts.getMergedDict(None,temp1,temp2)
print(type(temp))

for k,v in temp.items():
    print(k,v)




