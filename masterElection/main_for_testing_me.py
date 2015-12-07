#! /usr/bin/python3

from util.listhandler import *

print("test printing")

iein_eintrag = Entry(False, "testname")
zweiter_eintrag = Entry(False, "test....")

a_dict = {'192.168.0.212':iein_eintrag, '10.0.0.87':zweiter_eintrag}

print(a_dict.items())



#iein_eintrag.name = "test..."

print(iein_eintrag.name)
print("blablub")

