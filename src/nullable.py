from typing import TypeVar, Generic

T = TypeVar('T')

class nullable(Generic[T]):
    def __init__(self, value: T | None):
        self.__value = value

    @property
    def has_value(self) -> bool:
        return self.__value is not None
    
    @property
    def value(self) -> T:
        if self.has_value:
            return self.__value
        else:
            raise Exception()
    
    def get_value_or_default(self, default_value: T):
        return self.value if self.has_value else default_value
    
    def __str__(self):
        return self.value.__str__() if self.has_value else 'None'
    
    def __eq__(self, other):
        return self.value == other.value if (self.has_value and other.has_value) else False
    
    def __ne__(self, other):
        return not self.__eq__(other)

