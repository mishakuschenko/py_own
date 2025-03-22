class LexerException(Exception):
    def __init__(self, message=None, row=None, col=None) -> None:
        if row is not None and col is not None and message is not None:
            super().__init__(f"[{row}:{col}] {message}")
        else:
            super().__init__(message)

class ParserException(Exception):
    def __init__(self, string: str) -> None:
        super().__init__(string)

