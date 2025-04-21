class Action:
    def __init__(self):
        self.__handlers = set()

    @property
    def count(self):
        return self.__handlers.__len__()

    def fire(self, *args, **kwargs):
        for handler in self.__handlers:
            handler(*args, **kwargs)

    def add(self, handler):
        self.__handlers.add(handler)

    def remove(self, handler):
        self.__handlers.remove(handler)

    # def __iadd__(self, handler):
    #     self.add(handler)

    # def __isub__(self, handler):
    #     self.remove(handler)
