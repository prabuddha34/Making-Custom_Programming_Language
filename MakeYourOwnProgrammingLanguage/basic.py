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
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()

            if pos_end:
                self.pos_end = pos_end.copy()

            self.pos_end.advance()

    def __repr__(self):
        if self.value is not None:
            return f'{self.type}:{self.value}'
        return f'{self.type}'


#########
# Errors
#########

class Error:
    def __init__(self, error_name, details, line, column):
        self.error_name = error_name
        self.details = details
        self.line = line
        self.column = column

    def as_String(self):
        return (
            f"{self.error_name}: {self.details} "
            f"(Line {self.line}, Column {self.column})"
        )


class IllegalCharError(Error):
    def __init__(self, details, line, column):
        super().__init__(
            "Illegal Character",
            details,
            line,
            column
        )


class InvalidSyntaxError(Error):
    def __init__(self, details, line, column):
        super().__init__(
            "Invalid Syntax",
            details,
            line,
            column
        )


##########################
# LEXER
##########################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.curr = None

        self.line = 1
        self.column = 0

        self.advance()

    def advance(self):
        self.pos += 1

        if self.pos < len(self.text):
            self.curr = self.text[self.pos]

            if self.curr == '\n':
                self.line += 1
                self.column = 0
            else:
                self.column += 1
        else:
            self.curr = None

    def lets_cook_tokens(self):
        tokens = []
        errors = []

        while self.curr != None:

            if self.curr in ' \t\n':
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
                    IllegalCharError(
                        f"'{self.curr}'",
                        self.line,
                        self.column
                    )
                )
                self.advance()

        tokens.append(Token(TT_EOF))

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

        return Token(TT_FLOAT, float(num_str))


##########################
# RUN
##########################

def run(text):
    lexer = Lexer(text)
    tokens, errors = lexer.lets_cook_tokens()

    return tokens, errors


######
# Nodes
########

class NumberNodes:  # Hey lol so this is for th Numbers in our language
    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'


class BinOp:  # and this is for the binary ops such as 1+2 like this !!
    def __init__(self, left_node, op_token, right_node):
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node} {self.op_token} {self.right_node})'

        # here left means 1+2 so here left is 1 and op_token is '+' ok? and 2 is the right node


######## Parser Result


########### Helps to check that the parser result is true or not ?

class ParserResult:
    def __init__(self):
        self.error = None
        self.node = None

    def registers(self, res):

        if isinstance(res, ParserResult):

            if res.error:
                self.error = res.error

            if res.node:
                self.node = res.node

        return res

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        self.error = error
        return self


##############################

#### Parser it will do this 123+245= ans (cal) it


###############################

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.current_tok = None
        self.advance()

    def advance(self):
        self.tok_idx += 1

        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        else:
            self.current_tok = None

    def factor(self):

        res = ParserResult()
        tok = self.current_tok

        if tok.type in (TT_INT, TT_FLOAT):  # checking the data type of it

            self.advance()  # go to the next node

            return res.success(
                NumberNodes(tok)
            )  # of the value this is the

        return res.failure(
            InvalidSyntaxError(
                "Expected number",
                tok.line if hasattr(tok, 'line') else 1,
                tok.column if hasattr(tok, 'column') else 0
            )
        )

    def bin_op(self, func, ops):

     res = ParserResult()

     left = res.registers(func())

     if res.error:
         return res

     left = left.node

     while self.current_tok.type in ops:

        op_tok = self.current_tok

        self.advance()

        right = res.registers(func())

        if res.error:
            return res

        right = right.node

        left = BinOp(
            left,
            op_tok,
            right
        )

     return res.success(left)

    def term(self):

        return self.bin_op(
            self.factor,
            (TT_MUL, TT_DIV)
        )

    def expr(self):

        return self.bin_op(
            self.term,
            (TT_PLUS, TT_MINUS)
        )

    ## Parse Function to join them

    def parse(self):

        res = self.expr()

        if res.error:
            return res

        if self.current_tok.type != TT_EOF:

            return res.failure(
                InvalidSyntaxError(
                    "Expected '+', '-', '*', '/' or end of expression",
                    1,
                    0
                )
            )

        return res


##########################
# TERMINAL
##########################

while True:

    text = input("PraxLang >>> ")

    if text == "exit":
        print("Bye 👋")
        break

    tokens, errors = run(text)

    if errors:

        for error in errors:
            print(
                f"\033[91m[ERROR]\033[0m "
                f"{error.as_String()}"
            )

    else:

        parser = Parser(tokens)
        result = parser.parse()

        if result.error:

            print(
                f"\033[91m[ERROR]\033[0m "
                f"{result.error.as_String()}"
            )

        else:

            print(
                f"\033[92m[AST]\033[0m "
                f"{result.node}"
            )