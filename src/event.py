# https://www.educba.com/python-event-handler/
class Event(object):
    def __init__(self):
        self.__handlers = []

    def __iadd__(self, handler):
        self.__handlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__handlers.remove(handler)
        return self

    def __call__(self, *args, **keywargs):
        for _handler in self.__handlers:
            _handler(*args, **keywargs)
