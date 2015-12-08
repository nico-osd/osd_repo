#! /usr/bin/python3

import logging

logging.basicConfig(format='[%(asctime)s] [%(name)s] %(levelname)s: %(message)s', level=logging.DEBUG)


class Log(object):
    @staticmethod
    def get_logger(name=None, obj=None):
        if name:
            return logging.getLogger(name)
        elif obj:
            return logging.getLogger(obj.__class__.__name__)

    @staticmethod
    def debug(obj, *args):
        Log.get_logger(obj=obj)
        logging.debug(args[0], *args)

    @staticmethod
    def warning(obj, *args):
        logger = Log.get_logger(obj=obj)
        logger.warning(args[0], *args)

    @staticmethod
    def info(obj, *args):
        logger = Log.get_logger(obj=obj)
        logger.info(args[0], *args)
