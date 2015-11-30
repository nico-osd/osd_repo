# osd_repo
Das Ziel des Repositories ist die Zusammenarbeit an dem, in Python realisierten, Projekt der LV Open Source Development.


Das gewünschte Resultat: 

Ein Grid bestehend aus Raspberry Pis soll in der Lage sein, eine Aufgabe auf die vorhandenen Knoten zu verteilen und anschließend auszuwerten.

# Big Picture

Es wird eingeteilt in Broadcast (Gruppe 1), Master Election (Grp. 2) und Distribute Exercises (3 & 4) Pakete.

Etappen Ziele:
- Alle Raspis haben eine Liste für alle verbundenen Pis:
  - Name des Pis
  - IP-Adresse des Pis
  - Ist Master (y/n)
  - (To discuss: Pyro4 Objekt des Pis)
- Master wird verkündet
- Master verteilt Aufgaben an Pis

Darauf aufbauend:
- Master fällt aus, neue Master election
- Pis und Master fallen während der Ausführung von Aufgaben aus

# Roadmap

Prinzipiell ist dies eine Diskussionbasis und nicht in Stein gemeisselt.

## 10.12.15:


| Gruppe                                           | ToDo                                           |
| ------------------------------------------------ | ---------------------------------------------- |
| 1      | Raspis führen eine Liste von anderen Raspis im Netzwerk (siehe big picture)              |
| 2      | Prototyp Implementierung in (Pseudo-) Code oder Programmiersprache eurer Wahl            |
| 3 & 4  | Pyro4 Aufruf von Remote-Methoden ohne NameServer möglich                                 |

- [ ] Dokumentieren und definieren von Interfaces zwischen den Paketen.

## 17.12.15:

- [ ] Zusammenführen der Codebasis, falls notwendig
- [ ] testing testing testing

## 07.01.15:

- [ ] Mögliche Szenarien testen (Ausfall mehrerer Pis bzw. des Masters zu verschiedenen Zeitpunkten)

## 14.01.15:

- [ ] Implementierung ist 

# Dependencies

## 1. Pyro4 (auf RasPi)

installiere serpent (Abh. v. Pyro4):
`$ sudo pip3 install serpent`


installiere pyro4: 
`$ sudo pip3 install pyro4`
