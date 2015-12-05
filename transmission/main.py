#! /usr/bin/python3
from __future__ import print_function
import sys
import threading
import time
from socketserver import TCPServer
import Pyro4
from transmission.client.client import Client, TCPSender, Contact
from transmission.server.server import SingleTCPHandler, Server, send_server_uri

if sys.version_info < (3, 0):
    input = raw_input

sys.excepthook = Pyro4.util.excepthook


def main():
    sys.excepthook = Pyro4.util.excepthook

    print("Welcome to the prototype !\n")

    print("Would you like to be [s]erver or [c]lient? (s/c)")
    user_interaction = input(":> ").strip()

    if "s" == user_interaction:

        print("Please enter the IP-Address which the server should listen on.")
        ip_adr = input(":> ").strip()

        rl_ip_adr = Pyro4.socketutil.getInterfaceAddress(ip_adr)
        print("\nIMPORTANT: The Server will listen on: %s" % rl_ip_adr)

        HOST, PORT = rl_ip_adr, 20111

        daemon = Pyro4.Daemon(host=rl_ip_adr)
        srv_uri = daemon.register(Server())

        tcpserver = TCPServer((HOST, PORT),
                              lambda *args, **keys: SingleTCPHandler(send_server_uri, srv_uri.asString(), *args,
                                                                     **keys))

        t = threading.Thread(target=tcpserver.serve_forever)
        t.start()

        print("Serving...")
        daemon.requestLoop()

        tcpserver.shutdown()

    elif "c" == user_interaction:

        print("Please enter your name.")
        name = input(":> ").strip()

        print("Please enter the ip of the server.")
        srv_ip = input(":> ").strip()

        client = Client(name, srv_ip)

        clt_uri = client.get_uri().asString()

        TCPSender.send(clt_uri, (srv_ip, 20111))

        client.start()

        while client.is_running():
            time.sleep(1)

        contact = Contact(name, client.get_srv_uri())

        contact.register()

        input("Press Enter to exit.")

        contact.deregister()

if __name__ == '__main__':
    main()
