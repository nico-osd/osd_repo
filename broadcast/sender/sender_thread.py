#! /usr/bin/python3
from threading import Thread, Event
from time import sleep

from broadcast.sender.mulitcast_sender import MulticastSender
from util.config.logger import Log
from util.patterns.singletons import ListHandlerSingleton


class UDPSenderThread(Thread):
    """This Class represents a thread, which is continuously sending UDP-Multicasts in the defined timeout rhythm.
    """

    # Starting timeout
    TIMEOUT = 2

    # as we receive the first package, we want to expand the rhythm of sending the list.
    EXPANDED_TIMEOUT = 10

    def __init__(self):
        """Shall initialize the attributes and call the constructor of the super class.


        :return: None
        """
        super().__init__()
        self.runs = Event()

        # initial timeout
        self._timeout = self.TIMEOUT

        # the list handler singleton object to access the listhandler instance
        self.singleton = ListHandlerSingleton()

        # logger for logging purpose
        self.logger = Log.get_logger(name=self.__class__.__name__)

    def run(self):
        """Shall define what is executed within the thread.

        :return: None
        """

        # While Event().is_set() == False
        while self.is_running():
            # send the Thread sleeping
            sleep(self.timeout)

            # send a copy of the current listhandler _dict
            MulticastSender.send(self.singleton.handler.to_json())

    # TODO: send bye-msg, so the MC-Group is informed of this host's leaving

    def stop(self):
        """Shall set the Event Flag and stop the threads execution

        :return: None
        """
        self.runs.set()

    def is_running(self):
        """Shall return the threads status

        :return: True = running, False = stopped
        """
        return not self.runs.is_set()

    @property
    def timeout(self):
        """Shall return the currently defined timeout

        :return: the timeout attribute
        """
        return self._timeout

    def expand_timeout(self):
        """Shall set the Timeout attribute to the value of EXPANDED_TIMEOUT

        Only sets the value of the timeout attribute once to the value of the EXPANDED_TIMEOUT.
        If the value is already set - nothing is done.

        :return: None
        """
        if self.timeout == self.TIMEOUT:
            self._timeout = self.EXPANDED_TIMEOUT
