#! /usr/bin/python3


from util.listhandler import ListHandler


def main():
    handler = Singleton()


if __name__ == "__main__":
    main()


class Singleton(object):
    class __Singleton(object):
        def __init__(self):
            self.handler = ListHandler()

    instance = None

    def __new__(cls, *args, **kwargs):
        if not Singleton.instance:
            Singleton.instance = Singleton.__Singleton()
        return Singleton.instance

    def __getattr__(self, item):
        return getattr(self.instance, item)
