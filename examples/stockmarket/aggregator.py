#! /usr/bin/python3


class Aggregator(object):
    def __init__(self):
        """
        initializes attributes
        """
        # Dictionary of current viewers of this aggregator
        self.viewers = {}
        # List of symbols for this aggregator
        self.symbols = []

    def add_symbols(self, symbols):
        """
        Add the symbols to the attribute
        :param symbols: a List of symbols to append to the attribute
        """
        self.symbols.extend(symbols)

    def available_symbols(self):
        """
        returns the symbols attribute
        :return: None
        """
        return self.symbols

    def view(self, viewer, symbols):
        """
        Add the viewer as key and set the symbols as value
        :param viewer: the viewer of this aggregator
        :param symbols: the symbols which the viewer wants to view
        """
        self.viewers[viewer] = symbols

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
            for viewer, symbols in self.viewers.items():
                # has the viewer subscribed to the the current symbol (of the stockquote)
                # falls sich das symbol aus dem Stockquote in den Symbolen des Viewers befindet
                if symbol in symbols:
                    # print the value of the symbol at the market.
                    viewer.quote(market, symbol, value)
