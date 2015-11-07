#! /usr/bin/python3

from __future__ import print_function
import sys
from examples.stockmarket import stockmarket
from examples.stockmarket import aggregator
from examples.stockmarket import viewer

if sys.version_info < (3, 0):
    input = raw_input


def main():
    markets = stockmarket.main()
    aggr = aggregator.main(markets)
    viewer.main(aggr)

    print("\nPress enter to Quit.\n")
    input()


# run main if called
if __name__ == '__main__':
    main()
