#! /usr/bin/python3
from __future__ import print_function
import sys
import time
import random
import Pyro4

from transmission.client import Client
from transmission.server import Server

if sys.version_info < (3, 0):
    input = raw_input


def main():

    sys.excepthook = Pyro4.util.excepthook

    print("Welcome to the prototype !\n")

    print("What's your name?")
    name = input(":> ").strip()

    print("Enter your IP-Address:")
    host = input(":> ").strip()

    daemon = Pyro4.Daemon(host=host)

    print("Would you like to be [s]erver or [c]lient? (s/c)")
    user_interaction = input(":> ").strip()

    print("As Pyro does not provide a  functionality to stop it:")
    print("kill with Ctrl-C.")

    if "s" == user_interaction:
        server = Server()
        server_uri = daemon.register(server)

        ns = Pyro4.locateNS()
        ns.register("transmission.server", server_uri)

        daemon.requestLoop()

    elif "c" == user_interaction:
        client = Client(name)

        client.connect(host=host)
        client.register()

        daemon.requestLoop()

        client.deregister()

if __name__ == '__main__':
    main()
