#! /usr/bin/python3
import random


class StockMarket(object):
    def __init__(self, marketname, symbols):
        """
        initialize attributes and sets mean of symbols
        :param marketname: the name of the market (e.g. ATX, NYSE, etc.)
        :param symbols: the symbols of this market (e.g. GOOG, AAPL, etc.)
        """
        self.name = marketname
        self.symbolmeans = {}
        for symbol in symbols:
            self.symbolmeans[symbol] = random.uniform(20, 200)
        self.aggregators = []

    def generate(self):
        """
        sets the current quotes for symbols of this market
        """
        quotes = {}
        for symbol, mean in self.symbolmeans.items():
            if random.random() < 0.2:
                quotes[symbol] = round(random.normalvariate(mean, 20), 2)
        for aggregator in self.aggregators:
            aggregator.quotes(self.name, quotes)

    def listener(self, aggregator):
        """
        Append an aggregator
        :param aggregator: an aggregator (or listener) to append
        """
        self.aggregators.append(aggregator)

    def symbols(self):
        """
        Return the symbols of this stockmarket.
        :return: The symbols of this particular stockmarket.
        """
        return self.symbolmeans.keys()
