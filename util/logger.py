#! /usr/bin/python3

import logging

logging.basicConfig(format='[%(asctime)s] [%(name)s] %(levelname)s: %(message)s', level=logging.DEBUG)


def get_logger(name=None):
    return logging.getLogger(name)
