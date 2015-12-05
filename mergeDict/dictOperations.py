#!/usr/bin/python3

#from mergeDict.myDict import MyList

import datetime
import time

from examples.comparison.main import generate

# zuerst einmal nicht objektorinitiert
# 2 listen generieren


# das ist die Liste, wie sie aussehen wird
# bitte verwende diese
# by: Nico
rl_list = generate()

liste1 = dict()
liste2 = dict()


liste1 = {'10.20.0.200': ['raspi_streiter', 'F', '2015-11-27 20:36:10']}
liste1.update({'10.20.0.201': ['raspi_xxx', 'F', '2015-11-27 20:35:11']})
liste1.update({'10.20.0.198': ['raspi_yyy', 'T', '2015-11-27 20:37:20']})

liste2 = {'10.20.0.200': ['raspi_aaa', 'F', '2015-11-27 19:36:10']}
liste2.update({'10.20.0.101': ['raspi_bbb', 'F', '2015-11-27 20:34:58']})
liste2.update({'10.20.0.102': ['raspi_ccc', 'F', '2015-11-27 20:33:34']})


print('Das ist Liste 1: \n')

for a,b in liste1.items():
     print(a,b)


print('\nDas ist Liste 2: \n')

for a,b in liste2.items():
     print(a,b)

# dann listen mergen, ohne irgendwas zu checken

liste3 = liste1.copy()  #kopie von liste1 erstellen
liste3.update(liste2) #liste2 dazu mergen

print('\nDas ist die gemergede liste\n')

for a,b in liste3.items():
    print(a,b)

#man beachte, dass die werte unique sind !!!!

# nun objekt mit timestamp > 5 minuten entfernen ...

ts = time.time()

st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
print('\naktueller Timestamp - unformatiert\n')
print(ts)


# bringt aber nichts wegen beispielen
# erster approach: zu fuss

st1='2015-11-27 20:38:20'
st2='2015-11-27 20:24:00'

t1 = datetime.datetime.strptime(st1, "%Y-%m-%d %H:%M:%S")
t2 = datetime.datetime.strptime(st2, "%Y-%m-%d %H:%M:%S")

print('zeit1:',t1)
print('\nzeit2:',t2)
print(type(t1))

delta = t1 - t2

print('\n')
print('differenz\n')

print(delta)

# so nun vergleichen mit jedem eintrag der liste
# ich bleibe bei t1 als fixwert und vergleiche den mit jedem eintrag

#zuerst den value rauskitzeln

# neue liste machen
liste4 = liste3.copy()


# achtung ich gehe im folgenden nur durch die values !


#for v in liste3.values():
#    print(v[2])   # ist value auf index postition 2 ... also time
#    savedTime = datetime.datetime.strptime(v[2], "%Y-%m-%d %H:%M:%S").timestamp()
#    referenceTime = datetime.datetime.strptime(st1, "%Y-%m-%d %H:%M:%S").timestamp()
#    #delta = referendeTime - savedTime
#    delta = referenceTime - savedTime
#    print(delta)
#    # delta von 300 entspricht 5 minuten
#    if delta < 300:
#        print('delta ist grösser 5 minuten')

# nun das ganue mit dem kompletten dict

for k,v in liste3.items():

    savedTime = datetime.datetime.strptime(v[2], "%Y-%m-%d %H:%M:%S").timestamp()
    referenceTime = datetime.datetime.strptime(st1, "%Y-%m-%d %H:%M:%S").timestamp()
    # delta = referendeTime - savedTime
    delta = referenceTime - savedTime
    print(delta)
    if delta > 300:
        print(k,v)
        print(type(k))
        liste4.pop(k)

# neue liste ohne alter einträge
print('\nNeue Liste ohne alter Einträge älter als 5 Minuten: \n')

for k,v in liste4.items():
    print(k,v)







