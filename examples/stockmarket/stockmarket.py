#! /usr/bin/python3

from __future__ import print_function
import random
import threading
import time


class StockMarket(object):
    def __init__(self, marketname, symbols):
        """
        initialize attributes and sets mean of symbols
        :param marketname: the name of the market (e.g. ATX, NYSE, etc.)
        :param symbols: the symbols of this market (e.g. GOOG, AAPL, etc.)
        """
        self._name = marketname
        self._symbolmeans = {}
        for symbol in symbols:
            self._symbolmeans[symbol] = random.uniform(20, 200)
        self._aggregators = []

    def generate(self):
        """
        sets the current quotes for symbols of this market
        """
        quotes = {}
        for symbol, mean in self._symbolmeans.items():
            if random.random() < 0.2:
                quotes[symbol] = round(random.normalvariate(mean, 20), 2)
        print("new quotes generated for", self._name)
        for aggregator in self._aggregators:
            aggregator.quotes(self._name, quotes)

    def listener(self, aggregator):
        """
        Append an aggregator
        :param aggregator: an aggregator (or listener) to append
        """
        print("market {0} adding new aggregator".format(self._name))
        self._aggregators.append(aggregator)

    def symbols(self):
        """
        Return the symbols of this stockmarket.
        :return: The symbols of this particular stockmarket.
        """
        return self._symbolmeans.keys()

    def run(self):
        """
        Create and call Thread to generate new quotes
        """

        def generate_symbols():
            while True:
                time.sleep(random.random())
                self.generate()

        thread = threading.Thread(target=generate_symbols)
        thread.setDaemon(True)
        thread.start()


def main():
    """
    Create stockmarkets and run the Thread
    """
    symbols = ["AAPL", "CSCO", "MSFT", "GOOG"]
    nasdaq = StockMarket("NASDAQ", symbols)

    symbols = ["IBM", "HPQ", "BP"]
    newyork = StockMarket("NYSE", symbols)

    nasdaq.run()
    newyork.run()
    return [nasdaq, newyork]
