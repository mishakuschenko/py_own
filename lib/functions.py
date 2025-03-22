from lib.values import NumberValue
from values import Value
from typing import List
from parser.ast.statements import Statement

class Function:
    def execute(self, *args: List[Value]) -> Value:
        pass


class Functions:
    functions = {}

    @staticmethod
    def is_exists(key: str) -> bool:
        return key in Functions.functions

    @staticmethod
    def get(key: str) -> Function:
        if not Functions.is_exists(key): raise Exception(f"Unknown function: {key}")
        return Functions.functions[key]

    @staticmethod
    def set(key: str, func: Function):
        Functions.functions[key] = func


class UserDefinedFunction(Function):
    def __init__(self, arg_names: List[str], body: Statement) -> None:
        self.arg_names = arg_names
        self.body = body

    def get_arg_count(self) -> int:
        return len(self.arg_names)

    def get_args_name(self, index: int) -> str:
        if index < 0 or index >= self.get_arg_count():
            return ""
        return self.arg_names[index]

    def execute(self, *args: List[Value]) -> Value:
        try:
            self.body.execute()
            return NumberValue.zero
        except ReturnStatement as rt:
            return rt.get_result()

