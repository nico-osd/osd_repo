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
        if len(args) > 1:
            logging.debug(args[0], *args)
        else:
            logging.debug(args[0])

    @staticmethod
    def warning(obj, *args):
        logger = Log.get_logger(obj=obj)
        if len(args) > 1:
            logger.warning(args[0], *args)
        else:
            logger.warning(args[0])

    @staticmethod
    def info(obj, *args):
        logger = Log.get_logger(obj=obj)
        if len(args) > 1:
            logger.info(args[0], *args)
        else:
            logger.info(args[0])
