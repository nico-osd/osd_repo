#!/bin/python3

import time

from mergeDict.compareDict import TwoDicts
from util.listhandler import ListHandler

list1 = ListHandler()
list2 = ListHandler()

# create Entries

# by Nico:
# Creating entries for testing purpose shall be done by the generate method.
# Do not copy the ListHandler Class/File into your working directory.
# Import the version in util/listhandler
# you are creating duplicates and maintaining two different versions is not our goal
# please use the implementation in util and import it.


# The Entry is an object of the type Entry() which is implmented
# in the listhandler file.
# Please use the Entry Class over giving the handler an list.
# I will add functionality to take care of this and it will not
# accept any other type than Entry. I thought it would be clear
# due to the main method example.


list1.add_or_override_entry('10.20.0.200',entry=['FALSE','raspi_aaa','pyrouri',time.time()])
list1.add_or_override_entry('10.20.0.199',entry=['FALSE','raspi_bbb','pyrouri',time.time()-150])
list1.add_or_override_entry('10.20.0.19',entry=['FALSE','raspi_ccc','pyrouri',time.time()-250])

list2.add_or_override_entry('10.20.0.200',entry=['FALSE','raspi_ddd','pyrouri',time.time()])
list2.add_or_override_entry('10.20.0.23',entry=['FALSE','raspi_eee','pyrouri',time.time()-350])
list2.add_or_override_entry('10.20.0.1',entry=['FALSE','raspi_fff','pyrouri',time.time()-270])

# create temporary dicts from list handlers

# by Nico:
# get_dict will be removed and the handler is there to access the list
# you should never ever touch the dict directly as there might be
# multithread support. The handler will implement locking states
# and it is not supported by the dict it self.

# removed the method get_dict as it was for testing purpose.
# please do not use the dictionary it self as stated above.
temp1 = list1.get_dict()
temp2 = list2.get_dict()

# print(type(temp1))

# merge dicts

temp = TwoDicts.getMergedDict(None,temp1,temp2)
print(type(temp))

for k,v in temp.items():
    print(k,v)
