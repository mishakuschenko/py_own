class Expression:
    def eval(self) -> None:
        pass


class ArrayAccessExpression(Expression):
    def __init__(self, variable: str, indices: list[Expression]):
        self.variable = variable
        self.indices = indices

    def eval(self) -> None:
        return

