import datetime
from typing import Optional

class Stopwatch:
    def __init__(self, auto_start: bool = False):
        self.__start_ticks: Optional[int] = None
        self.__end_ticks: Optional[int] = None

        if auto_start:
            self.start()

    def __datetime_to_ticks(dt):
        return (dt - datetime(1, 1, 1)).total_seconds() * 10000000

    @property
    def __current_ticks(self):
        return __datetime_to_ticks(datetime.utcnow())

    @property
    def is_running(self):
        return self.__start_ticks != None and self.__end_ticks == None

    @property
    def ticks(self):
        return (self.__end_ticks - self.__start_ticks)

    def start(self):
        self.__start_ticks = self.__current_ticks

    def stop(self):
        self.__end_ticks = self.__current_ticks

    def reset(self):
        self.__start_ticks = None
        self.__end_ticks = None

    def __str__(self):
        return f'aaa'