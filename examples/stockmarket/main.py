#! /usr/bin/python3

from __future__ import print_function
import time
from examples.stockmarket.stockmarket import StockMarket
from examples.stockmarket.aggregator import Aggregator
from examples.stockmarket.viewer import Viewer


def main():
    """
    Runs stockmarkets, aggregators and viewers for aggregators.
    """
    # Create NASDAQ Stockmarket with the following symbols
    symbols = ["AAPL", "CSCO", "MSFT", "GOOG"];
    nasdaq = StockMarket("NASDAQ", symbols)

    # Create New York Stock Exchange with the following symbols
    symbols = ["IBM", "HPQ", "BP"]
    newyork = StockMarket("NYSE", symbols)

    # create an aggregator with all symbols of both markets
    agg = Aggregator()
    agg.add_symbols(nasdaq.symbols())
    agg.add_symbols(newyork.symbols())
    # print the symbols aggregated
    print("aggregated symbols: ", agg.available_symbols())

    # register the aggregator as listener for the stockmarkets
    nasdaq.listener(agg)
    newyork.listener(agg)

    # create viewer with interesting Symbols (marketplace is irrelevant)
    view = Viewer()
    symbols = ["AAPL", "GOOG", "BP"]

    # set which symbols should be viewed
    agg.view(view, symbols)
    print("")

    # start generating quotes - for ever.
    while True:
        nasdaq.generate()
        newyork.generate()
        time.sleep(0.5)

# run main if called
if __name__ == '__main__':
    main()
