
class Value:
    def as_number(self):
        pass

    def as_string(self):
        pass


class ArrayValue(Value):
    def __init__(self, size: int=None, elements: list[Value]=None) -> None:
        if size is not None:
            self.size = size
        elif elements is not None:
            self.elements = elements.copy()

    def get(self, index: int) -> Value:
        return self.elements[index]

    def set(self, index: int, value: Value) -> None:
        self.elements[index] = value

    def as_number(self) -> float:
        raise Exception("Cannot cast array to number")

    def as_string(self) -> str:
        return str(self.elements)


class NumberValue(Value):
    zero = None
    one = None

    @staticmethod
    def from_boolean(self, b: bool):
        return NumberValue.one if b else NumberValue.zero

    def __init__(self, value: float) -> None:
        self.value = value

    def as_number(self) -> float:
        return self.value

    def as_string(self) -> str:
        return str(self.value)

    def __str__(self) -> str:
        return self.as_string()



class StringValue(Value):
    def __init__(self, value: str) -> None:
        self.value = value

    def as_number(self) -> float:
        try:
            return float(self.value)
        except Exception:
            return 0

    def as_string(self) -> str:
        return self.value

    def __str__(self):
        return self.as_string()
    