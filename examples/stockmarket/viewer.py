#! /usr/bin/python3

from __future__ import print_function
import sys
import Pyro4

if sys.version_info < (3, 0):
    input = raw_input


class Viewer(object):
    def quote(self, market, symbol, value):
        """
        Print the current quote of the symbol at the given market
        :param market: the stockmarket with the symbol the viewer subscribed
        :param symbol: the symbol at the stockmarket the viewer specified
        :param value: the current value of the quote
        """
        print("{0}.{1}: {2}".format(market, symbol, value))


def main():
    """
    Register a new viewer at the aggregator.
    :param aggregator: The aggregator to register this viewer.
    :return: viewer - The freshly created viewer object for the symbols.
    """

    # Create Viewer Object
    viewer = Viewer()

    # Create Pyro4 Daemon to register viewer object
    daemon = Pyro4.Daemon()
    daemon.register(viewer)

    # Proxy aggregator object with the given pyro-name
    # as there is only one aggregator object at the
    # name server registered, we dont need to loop over
    # a dict of object->uri pairs (as seen in aggregator.py)
    aggregator = Pyro4.Proxy("PYRONAME:examples.stockmarket.aggregator")

    print("Available stock symbols: ", aggregator.available_symbols())

    # let the user choose some symbols
    symbols = input("Enter Stocksymbols you want to view (comma seperated):\n\ninput>")
    symbols = [symbol.strip() for symbol in symbols.split(",")]

    # tell the aggregator to view the chosen symbols for this viewer object.
    aggregator.view(viewer, symbols)
    print("Viewer listening on symbols", symbols)

    daemon.requestLoop()


if __name__ == '__main__':
    main()
