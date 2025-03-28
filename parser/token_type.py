from enum import Enum


class TokenType(Enum):
    NUMBER = "NUMBER"
    HEX_NUMBER = "HEX_NUMBER"
    WORD = "WORD"
    TEXT = "TEXT"

    # keywords
    PRINT = "PRINT"
    PRINTLN = "PRINTLN"
    IF = "IF"
    ELSE = "ELSE"
    WHILE = "WHILE"
    FOR = "FOR"
    DO = "DO"
    BREAK = "BREAK"
    CONTINUE = "CONTINUE"
    FUN = "FUN"
    RETURN = "RETURN"
    USE = "USE"
    MATCH = "MATCH"
    CASE = "CASE"
    EXTRACT = "EXTRACT"
    INCLUDE = "INCLUDE"
    CLASS = "CLASS"
    NEW = "NEW"

    # operators
    PLUS = "+"
    MINUS = "-"
    STAR = "*"
    SLASH = "/"
    PERCENT = "%"
    AT = "@"

    EQ = "="
    EQEQ = "=="
    EXCL = "!"
    EXCLEQ = "!="
    LTEQ = "<="
    LT = "<"
    GT = ">"
    GTEQ = ">="

    PLUSEQ = "+="
    MINUSEQ = "-="
    STAREQ = "*="
    SLASHEQ = "/="
    PERCENTEQ = "%="
    ATEQ = "@="
    AMPEQ = "&="
    CARETEQ = "^="
    BAREQ = "|="
    COLONCOLONEQ = "::="
    LTLTEQ = "<<="
    GTGTEQ = ">>="
    GTGTGTEQ = ">>>="

    PLUSPLUS = "++"
    MINUSMINUS = "--"

    LTLT = "<<"
    GTGT = ">>"
    GTGTGT = ">>>"

    DOTDOT = ".."
    STARSTAR = "**"
    QUESTIONCOLON = "?:"
    QUESTIONQUESTION = "??"

    TILDE = "~"
    CARET = "^"
    CARETCARET = "^^"
    BAR = "|"
    BARBAR = "||"
    AMP = "&"
    AMPAMP = "&&"

    QUESTION = "?"
    COLON = ":"
    COLONCOLON = "::"

    LPAREN = "("
    RPAREN = ")"
    LBRACKET = "["
    RBRACKET = "]"
    LBRACE = "{"
    RBRACE = "}"
    COMMA = ","
    DOT = "."

    EOF = "EOF"
