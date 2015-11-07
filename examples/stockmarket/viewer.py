#! /usr/bin/python3

from __future__ import print_function


class Viewer(object):
    def quote(self, market, symbol, value):
        """
        Print the current quote of the symbol at the given market
        :param market: the stockmarket with the symbol the viewer subscribed
        :param symbol: the symbol at the stockmarket the viewer specified
        :param value: the current value of the quote
        """
        print("{0}.{1}: {2}".format(market, symbol, value))


def main(aggregator):
    """
    Register a new viewer at the aggregator.
    :param aggregator: The aggregator to register this viewer.
    :return: viewer - The freshly created viewer object for the symbols.
    """
    viewer = Viewer()
    symbols = ["BP", "HPQ", "MSFT", "GOOG"]
    aggregator.view(viewer, symbols)
    return viewer