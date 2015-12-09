#! /usr/bin/python3


from util.listhandler import ListHandler, Entry
from util.logger import Log
from util.networking import get_ip_address

INTERFACE_NAME = "wlan0"


def main():
    singleton = Singleton()
    logger = Log.get_logger("main")

    try:
        # determine current ip-address of the interface wlan0
        wlan_ip_addr = get_ip_address(INTERFACE_NAME)
    except OSError:
        logger.error("Not connected to any network on adapter %s. Please check the connection of %s.", INTERFACE_NAME,
                     INTERFACE_NAME)
        exit(1)
    logger.info("Selected network address: %s", wlan_ip_addr)

    # add own ip + empty Entry object to dict
    singleton.handler.add_or_override_entry(wlan_ip_addr, Entry())


class Singleton(object):
    class __Singleton(object):
        def __init__(self):
            self.handler = ListHandler()

    instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)


if __name__ == "__main__":
    main()
