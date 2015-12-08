#! /usr/bin/python3

import random
import time

from util.listhandler import ListHandler, Entry

NETWORK = "10.20.0."


def main():
    """
    This main method is only for testing purpose and is going to be removed in the future.
    It prints the generated dict to console.
    """
    handler = generate()

    # print as json

    print(handler.to_json())


def generate():
    handler = ListHandler()
    is_master_elected = False

    for i in range(random.randrange(5, 15)):
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

        # set timestamp
        timestamp = int(time.time()) - random.randrange(0, 1000)

        # creating entry

        entry = Entry(is_master, name, "", timestamp) if random.random() < 0.7 else Entry()

        # adding entry

        print("ENTRY: ", end="")
        print(entry)

        handler.add_or_override_entry(ip, entry)

        print("Generated Entry #{}".format(i))

    return handler


if __name__ == '__main__':
    main()
