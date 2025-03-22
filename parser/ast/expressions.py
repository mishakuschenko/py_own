from lib.values import Value, ArrayValue, NumberValue, StringValue
from lib.variables import Variables
from parser.ast.node import Node
from parser.ast.visitor import Visitor
from typing import List
from enum import Enum

class Expression(Node):
    def eval(self) -> Value:
        pass


class ArrayAccessExpression(Expression):
    def __init__(self, variable: str, indices: List[Expression]):
        self.variable = variable
        self.indices = indices

    def eval(self) -> None:
        self.get_array().get(self.last_index())

    def get_array(self) -> ArrayValue:
        array = self.__consume_array(Variables.get(self.variable))
        last = len(self.indices)-1
        for i in range(last):
            array = self.__consume_array(array.get(self.__index(1)))
        return array

    def __index(self, index: int) -> int:
        return int(self.indices[index].eval().as_number())

    def last_index(self) -> int:
        return self.__index(len(self.indices) - 1)


    def __consume_array(self, value: Value) -> ArrayValue:
        if isinstance(value, ArrayValue):
            return value
        else:
            raise RuntimeError("Array expected")

    def accept(self, visitor: Visitor) -> None:
        visitor.visit(self)

    def __str__(self) -> str:
        return self.variable+str(self.indices)


class ArrayExpression(Expression):
    pass

class ConditionalExpression(Expression):
    class Operator(Enum):
        EQUALS = "=="
        NOT_EQUALS = "!="
        LT = "<"
        LTEQ = "<="
        GT = ">"
        GTEQ = ">="

        AND = "&&"
        OR = "||"

        def __init__(self, name: str) -> None:
            self.name = name

        def get_name(self) -> str:
            return self.name

    def __init__(self, operation: Operator, expr1: Expression, expr2: Expression) -> None:
        self.operation = operation
        self.expr1 = expr1
        self.expr2 = expr2

    def eval(self) -> Value:
        val1 = self.expr1.eval()
        match self.operation:
            case self.Operator.OR:
                return NumberValue.from_boolean((val1.as_number() != 0) or (self.expr2.eval().as_number() != 0))
            case self.Operator.AND:
                return NumberValue.from_boolean((val1.as_number() != 0) and (self.expr2.eval().as_number() != 0))


        val2 = self.expr2.eval()
        num1: float
        num2: float

        if isinstance(val1, StringValue):
            num1 = (val1.as_string() > val2.as_string()) - (val1.as_string() < val2.as_string())
            num2 = 0
        else:
            num1 = val1.as_number()
            num2 = val2.as_number()

        res: bool
        match self.operation:
            case self.Operator.EQUALS: res = num1 == num2
            case self.Operator.NOT_EQUALS: res = num1 != num2
            case self.Operator.LT: res = num1 < num2
            case self.Operator.LTEQ: res = num1 <= num2
            case self.Operator.GT: res = num1 > num2
            case self.Operator.GTEQ: res = num1 >= num2

            case _: raise RuntimeError(f"Operation {self.operation} is not supported")

        return NumberValue.from_boolean(res)

    def accept(self, visitor: Visitor) -> None:
        visitor.visit(self)

    def __str__(self) -> str:
        return f"{self.expr1} {self.operation} {self.expr2}"


class BinaryExpression(Expression):
    pass


class UnaryExpression(Expression):
    pass


class TernaryExpression(Expression):
    pass