from tokens.token import Token


class Symbol(Token):
    """
    Represents a symbol
    """

    def __init__(self, value):
        Token.__init__(self, value)

    def __repr__(self):
        return self.value
