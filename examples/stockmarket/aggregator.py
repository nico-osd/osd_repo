#! /usr/bin/python3

from __future__ import print_function
import Pyro4


class Aggregator(object):
    def __init__(self):
        """
        initializes attributes
        """
        # Dictionary of current viewers of this aggregator
        self._viewers = {}
        # List of symbols for this aggregator
        self._symbols = []

    def add_symbols(self, symbols):
        """
        Add the symbols to the attribute
        :param symbols: a List of symbols to append to the attribute
        """
        self._symbols.extend(symbols)

    def available_symbols(self):
        """
        returns the symbols attribute
        :return: None
        """
        return self._symbols

    def view(self, viewer, symbols):
        """
        Add the viewer as key and set the symbols as value
        :param viewer: the viewer of this aggregator
        :param symbols: the symbols which the viewer wants to view
        """
        print("aggregator gets a new viewer, for symbols: ", symbols)
        self._viewers[viewer] = symbols

    def quotes(self, market, stockquotes):
        """
        update quotes for all viewers for subscribed symbols
        :param market: the market which updated its quotes
        :param stockquotes: the quotes of the symbols for this market
        """
        # iterate over all stockquotes and set the
        # symbol -> stockmarket symbol
        # value -> quote
        for symbol, value in stockquotes.items():
            # iterate over all viewers and set the
            # current key -> viewer
            # current value -> symbols of the viewer
            for viewer, symbols in self._viewers.items():
                # has the viewer subscribed to the the current symbol (of the stockquote)
                # falls sich das symbol aus dem Stockquote in den Symbolen des Viewers befindet
                if symbol in symbols:
                    # print the value of the symbol at the market.
                    viewer.quote(market, symbol, value)


def main():
    """
    Add symbols to aggragator and register as listener at stockmarket.
    :param stockmarkets: available stockmarkets
    :return: aggregator - The freshly created aggregator for the given stockmarkets.
    """

    # create an aggregator object
    aggregator = Aggregator()

    # create a pyro4 daemon to register aggregator object and get the uri
    daemon = Pyro4.Daemon()

    # register aggregator object and get object uri
    agg_uri = daemon.register(aggregator)

    # locate nameserver to register aggregator object at name server
    ns = Pyro4.locateNS()

    # register object at nameserver with a given name and an id (uri)
    ns.register("examples.stockmarket.aggregator", agg_uri, safe=True)

    # get all registered stockmarkets from the name server
    # to get a dict of all "object -> uri" pairs a prefix of the objects
    # is needed.
    for market, market_uri in ns.list(prefix="example.stockmarket.").items():
        print("subscribing to market ", market)
        # create Proxy object of stockmarket with the given uri
        stockmarket = Pyro4.Proxy(market_uri)
        # register aggregator at stockmarket
        stockmarket.listener(aggregator)
        # append symbols to aggregator
        aggregator.add_symbols(stockmarket.symbols())
    # we did not find any market if there are no symbols.
    if not aggregator.available_symbols():
        raise ValueError("no symbols found! (Are StockMarkets up and running?")

    print("Aggregator running! Symbols:", aggregator.available_symbols())
    daemon.requestLoop()

if __name__ == '__main__':
    main()
