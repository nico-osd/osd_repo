#! /usr/bin/python3

from __future__ import print_function
import time
from examples.stockmarket.stockmarket import StockMarket
from examples.stockmarket.aggregator import Aggregator
from examples.stockmarket.viewer import Viewer

def main():
    symbols = ["AAPL", "CSCO", "MSFT", "GOOG"];
    nasdaq = StockMarket("NASDAQ", symbols)

    symbols = ["IBM", "HPQ", "BP"]
    newyork = StockMarket("NYSE", symbol)

    agg = Aggregator()
    agg.add_symbols(nasdaq.symbols())
    agg.add_symbols(newyork.symbols())
    print("aggregated symbols: ", agg.available_symbols())

    nasdaq.listener(agg)
    newyork.listener(agg)

    view = Viewer()
    symbols = ["AAPL", "GOOG", "BP"]
    agg.view(view, symbols)
    print("")
    while True:
        nasdaq.generate()
        newyork.generate()
        time.sleep(0.5)

if __name__ == '__main__':
    main()
