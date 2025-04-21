from datetime import datetime, timedelta, timezone
from typing import Final
from nullable import nullable


class Chronograf:
    def __init__(self, *, auto_start=False) -> None:
        self.__start = nullable[datetime](None)
        self.__end = nullable[datetime](None)
        if auto_start:
            self.start()

    @property
    def __current_datetime(self) -> datetime:
        return datetime.now(_util.timezone)

    @property
    def is_running(self) -> bool:
        return self.__start.has_value and not self.__end.has_value

    @property
    def elapsed(self) -> nullable[timedelta]:
        match (self.__start.has_value, self.__end.has_value):
            case (True, False):
                return nullable(self.__current_datetime - self.__start.value)
            case (True, True):
                return nullable(self.__end.value - self.__start.value)
        return nullable[timedelta].null()

    def start(self) -> None:
        self.__start.value = self.__current_datetime

    def stop(self) -> None:
        if self.is_running:
            self.__end.value = self.__current_datetime

    def restart(self) -> None:
        self.reset()
        self.start()

    def reset(self) -> None:
        self.__start.value = None
        self.__end.value = None


class _util:
    timezone: Final = timezone.utc
