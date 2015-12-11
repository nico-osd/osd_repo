#! /usr/bin/python3

"""
from: http://www.nealc.com/blog/blog/2012/09/11/testing/

The SocketServer module does not provide support for multicast. This module
provides a subclass of SocketServer.UDPServer that can listen on multicast
addresses.

This only supports IPv4
"""

import socket
import socketserver
import struct


class ThreadedUDPMulticastServer(socketserver.ThreadingMixIn, socketserver.UDPServer):
    """Extends UDPServer to join multicast groups and bind
    the local interface properly
    """

    def __init__(self, multicast_address, request_handler_clazz,
                 listen_interfaces=None):
        """Create a new multicast server.

        multicast_address - two tuple ('multicast address', port)
        RequestHandlerClass - a SocketServer.BaseRequesetHandler
        listen_interfaces - list of local interfaces (identified by IP addresses)
        the server should listen on for multicast packets. If None,
        the system will decide which interface to send the multicast group join
        on
        """
        # to receive multicast packets, must bind the port,
        # set bind_and_active to True.
        # Note: some hosts don't allow bind()'ing to a multicast address,
        # so bind to INADDR_ANY
        socketserver.UDPServer.__init__(self, ('', multicast_address[1]),
                                        request_handler_clazz, True)

        # Note: struct ip_mreq { struct in_addr (multicast addr), struct in_addr
        # (local interface) }
        if listen_interfaces is None:
            mreq = struct.pack("4sI", socket.inet_aton(multicast_address[0]),
                               socket.INADDR_ANY)
            self.socket.setsockopt(socket.IPPROTO_IP,
                                   socket.IP_ADD_MEMBERSHIP, mreq)
        else:
            for interface in listen_interfaces:
                mreq = socket.inet_aton(
                    multicast_address[0]) + socket.inet_aton(interface)
                self.socket.setsockopt(socket.IPPROTO_IP,
                                       socket.IP_ADD_MEMBERSHIP, mreq)
