from abc import ABC, abstractmethod

class Value(ABC):
    @abstractmethod
    def as_number(self):
        pass

    @abstractmethod
    def as_string(self):
        pass


class ArrayValue(Value):
    pass


class NumberValue(Value):
    pass


class StringValue(Value):
    pass

