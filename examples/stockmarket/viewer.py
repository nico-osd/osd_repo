#! /usr/bin/python3

from __future__ import print_function


class Viewer(object):
    def quote(selfself, market, symbol, value):
        print("{0}.{1}: {2}".format(market, symbol, value))