#! /usr/bin/python3
import sys

from broadcast.manager import UDPManager
from examples.observer import ObserverInterface
from util.config.logger import Log
from util.config.statics import INTERFACE_NAME
from util.listhandler import Entry
from util.networking import get_ip_address
from util.patterns.singletons import ListHandlerSingleton, UDPObservableSingleton


class Observer(ObserverInterface):
    """Observer pattern: Implementation class for Observer"""
    def __init__(self, observed=''):
        super().__init__()
        self.list = []

    def subscribe_observed(self, observed):
        observed.add_observer(self)

    def unsubscribe_observed(self, observed):
        observed.remove_observer(self)

    def update(self, observable, arg):
        self.list.append(arg)
        # TODO: implement update function
        Log.info(self, "Data: %s", str(arg))


def main(argv):
    interface_name = None
    if len(argv) > 0:
        interface_name = argv[0]

    list_handler_singleton = ListHandlerSingleton()
    udp_observable_singleton = UDPObservableSingleton()

    logger = Log.get_logger("main")

    try:

        if interface_name:
            wlan_ip_addr = get_ip_address(interface_name)
        else:
            # determine current ip-address of the interface wlan0
            wlan_ip_addr = get_ip_address(INTERFACE_NAME)
    except OSError:
        logger.error("Not connected to any network on adapter %s. Please check the connection of %s.", INTERFACE_NAME,
                     INTERFACE_NAME)
        exit(1)
    logger.info("Selected network address: %s", wlan_ip_addr)

    # add own ip + empty Entry object to dict
    list_handler_singleton.handler.add_or_override_entry(wlan_ip_addr, Entry())

    udp_manager = UDPManager(wlan_ip_addr)

    udp_manager.start()

    observer = Observer()

    observer.subscribe_observed(udp_observable_singleton.observable)

    input("Enter to Exit.")

    udp_manager.stop()

if __name__ == "__main__":
    main(sys.argv[1:])