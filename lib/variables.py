from collections import deque
from values import NumberValue


class Variables:
    stack = deque()
    variables = {
        "true": NumberValue.one,
        "false": NumberValue.zero
    }

    @staticmethod
    def push() -> None:
        Variables.stack.append(Variables.variables.copy())

    @staticmethod
    def pop() -> None:
        if Variables.stack:
            Variables.variables = Variables.stack.pop()

    @staticmethod
    def is_exists(key: str) -> bool:
        return key in Variables.variables

    @staticmethod
    def get(key):
        if not Variables.is_exists(key):
            return NumberValue.zero
        return Variables.variables[key]

    @staticmethod
    def set(key, value) -> None:
        Variables.variables[key] = value