#! /usr/bin/python3
from masterElection.masterEle import ME
from util.listhandler import *
import copy
import socket

print("test printing")

iein_eintrag = Entry(False, "testname")
zweiter_eintrag = Entry(False, "test....")

a_dict = {'192.168.0.212':iein_eintrag, '10.0.0.87':zweiter_eintrag}

print(a_dict.items())

sec_dict = copy.deepcopy(a_dict)

print(sec_dict.items())
x = sec_dict.get('192.168.0.212')

x.name = "wasAnderes"
sec_dict['192.168.0.212'] = x

#iein_eintrag.name = "test..."

print(sec_dict.items())
print(sec_dict.get('192.168.0.212').name)
print("-----")
print(a_dict.items())
print(a_dict.get('192.168.0.212').name)

for k, v in a_dict.items():
    a_dict.get(k).is_master = True

print(a_dict.items())
print(a_dict.get('192.168.0.212').is_master)

hostnamex = socket.gethostname()
print(socket.gethostbyname(hostnamex))

print("----------------------------------------")

masterselect = ME()

another_dict = masterselect.select_master(sec_dict)
for k, v in another_dict.items():
    print(another_dict.get(k).is_master)
    print(another_dict.get(k).name)