#! /usr/bin/python3

import json
import random
import time

from util.listhandler import ListHandler, Entry, EntryEncoder

NETWORK = "10.20.0."


def main():
    """
    This main method is only for testing purpose and is going to be removed in the future.
    It generates list items and prints them to console.
    """
    handler = ListHandler()
    is_master_elected = False

    for i in range(random.randrange(5, 10)):
        # constructing entry parameters with some randomness
        ip = NETWORK + str(random.randrange(1, 255))

        # if there is no master
        if not is_master_elected:
            is_master = True if random.random() > 0.5 else False

            # if randomness selects this as master, set the flag.
            if is_master:
                is_master_elected = True

        # flag is set = there is already a master.
        else:
            is_master = False

        # just a placeholder
        name = "ip_" + str(ip)

        # executing this script has to be a pain.
        time.sleep(random.randrange(0, 3))

        # set timestamp
        timestamp = int(time.time())

        # creating entry

        entry = Entry(is_master, name, "", timestamp) if random.random() < 0.7 else Entry()

        # adding entry

        handler.add_or_override_entry(ip, entry)

        print("Generated Entry #{}".format(i))

    # print as json

    print(json.dumps(handler.get_dict(), sort_keys=True, indent=4, cls=EntryEncoder))


if __name__ == '__main__':
    main()
