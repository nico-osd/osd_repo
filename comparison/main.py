#! /usr/bin/python3

from comparison.listhandler import ListHandler, Entry, EntryEncoder
import random
import time
import json

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
        if not is_master_elected:
            is_master = True if random.random() > 0.5 else False
            if is_master:
                is_master_elected = True
        else:
            is_master = False

        name = "ip_" + str(ip)

        time.sleep(random.randrange(0, 3))

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
