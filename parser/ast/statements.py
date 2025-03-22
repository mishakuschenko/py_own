from expressions import Expression
from lib.values import Value
from node import Node
from parser.ast.visitor import Visitor


class Statement(Node):
    def execute(self) -> None:
        pass


class ArrayAssignmentStatement(Statement):
    pass


class BlockStatement(Statement):
    pass


class BreakStatement(Statement):
    pass


class ContinueStatement(Statement):
    pass


class DoWhileStatement(Statement):
    pass


class ForStatement(Statement):
    pass


class FunctionDefineStatement(Statement):
    pass


class FunctionStatement(Statement):
    pass


class IfStatement(Statement):
    pass


class PrintStatement(Statement):
    pass


class ReturnStatement(Statement, Exception):

    result: Value

    def __init__(self, expression: Expression) -> None:
        self.expression = expression

    def get_result(self) -> Value:
        return ReturnStatement.result

    def execute(self) -> None:
        ReturnStatement.result = self.expression.eval()
        raise self

    def accept(self, visitor: Visitor) -> None:
        visitor.visit(self)

    def __str__(self) -> str:
        return f"Return {self.expression}"


class UseStatement(Statement):
    pass


class WhileStatement(Statement):
    pass
