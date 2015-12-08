#!/bin/python3

import socket
import struct
import csv
import sys


def main():
    multicast_group = "224.0.0.1"
    server_address = ("", 10000)

    # Create the socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind to the server address
    sock.bind(server_address)

    # Tell the operating system to add the socket to the multicast group
    # on all interfaces.#
    group = socket.inet_aton(multicast_group)
    mreq = struct.pack("4sL", group, socket.INADDR_ANY)
    sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
    while True:
        print("\nwaiting to receive message")
        data, address = sock.recvfrom(1024)

        print("received ", len(data), " bytes from ", address)
        print("message: ", data)
        print("sending acknowledgement to ", address)
        sock.sendto("ack".encode("utf-8"), address)

        addip(address)


# NICHT in receive
def addip(address):
    iplist = []
    # if IP is not in the list, add it to the list and write it in the file
    if address[0] not in iplist:
        # temp IP list
        iplist.append(address[0])
        # f = open("iplist", "a")
        # f.write(address[0]+",")
        # f.close()
        # print("List updated and IP \"", address[0], "\" added.")


if __name__ == "__main__":
    main()