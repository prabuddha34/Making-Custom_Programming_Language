######################
# TOKENS
######################

TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'

TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'

TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'

TT_EOF = 'TT_EOF'

DIGITS = '0123456789'


class Token:
    def __init__(self, type_, value=None):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value is not None:
            return f'{self.type}:{self.value}'
        return f'{self.type}'


#########
# Errors
#########

class Error:
    def __init__(self, error_name, details):
        self.error_name = error_name
        self.details = details

    def as_String(self):
        return f'{self.error_name}:{self.details}'


class IllegalCharError(Error):
    def __init__(self, details):
        super().__init__(
            "Illegal Character Dwag chiill man dont do vibe code lol",
            details
        )


##########################
# LEXER
##########################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.curr = None

        self.advance()

    def advance(self):
        self.pos += 1
        self.curr = self.text[self.pos] if self.pos < len(self.text) else None

    def lets_cook_tokens(self):
        tokens = []
        errors = []

        while self.curr != None:

            if self.curr in ' \t':
                self.advance()

            elif self.curr == '+':
                tokens.append(Token(TT_PLUS, '+'))
                self.advance()

            elif self.curr == '-':
                tokens.append(Token(TT_MINUS, '-'))
                self.advance()

            elif self.curr == '*':
                tokens.append(Token(TT_MUL, '*'))
                self.advance()

            elif self.curr == '/':
                tokens.append(Token(TT_DIV, '/'))
                self.advance()

            elif self.curr == '(':
                tokens.append(Token(TT_LPAREN, '('))
                self.advance()

            elif self.curr == ')':
                tokens.append(Token(TT_RPAREN, ')'))
                self.advance()

            elif self.curr.isdigit():
                tokens.append(self.make_numbers_lol())

            else:
                errors.append(
                    IllegalCharError(f"'{self.curr}'")
                )
                self.advance()

        tokens.append(Token(TT_EOF, None))

        return tokens, errors

    def make_numbers_lol(self):

        num_str = ''
        dot_count = 0

        while self.curr != None and self.curr in DIGITS + '.':

            if self.curr == '.':

                if dot_count == 1:
                    break

                dot_count += 1

            num_str += self.curr
            self.advance()

        if dot_count == 0:
            return Token(TT_INT, int(num_str))

        else:
            return Token(TT_FLOAT, float(num_str))


def run(text):
    lexer = Lexer(text)
    tokens, errors = lexer.lets_cook_tokens()

    return tokens, errors