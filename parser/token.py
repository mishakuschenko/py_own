from token_type import TokenType


class Token:
    def __init__(self, token_type: TokenType, text: str, row: int, col: int) -> None:
        self.type = token_type
        self.text = text
        self.row = row
        self.col = col

    def get_type(self) -> TokenType:
        return self.type

    def get_text(self) -> str:
        return self.text

    def get_row(self) -> int:
        return self.row

    def get_col(self) -> int:
        return self.col

    def position(self) -> str:
        return f"[{self.row}:{self.col}]"

    def __str__(self) -> str:
        return f"{self.type.name} {self.position()} {self.text}"
