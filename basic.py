######################
# TOKENS
######################
import string
import sys
import os

TT_INT = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'

TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL' #lol it is boring to make a language of yours ?huh?
TT_DIV = 'TT_DIV'

TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'

TT_EOF = 'TT_EOF'

#Digits holder baby
DIGITS = '0123456789'


#VARiables man lol so need an identifiet

TT_IDENTIFIER='TT_IDENTIFIER'
TT_KEYWORD='TT_KEYWORD'
TT_EQ='TT_EQ'

#Custom token about my own gf (my cutie little girl)and I really love her

TT_SRI='TT_SRI'

KEYWORDS=[
    "V", #for naming the varaible,
    "AND", # this is the and one
    "OR", #this is the or one
    "NOT",#thi is the not one
    "IF", #If stament key word
    "THEN", #goes after the IF / ELIF condition
    "ELIF", #else if ladder
    "ELSE", #here the else block will be executed of there
    "FOR",
    "TO",
    "WHILE",
    "PRINT",
    "print"
]
#add some realtional and conditional ones in my language so get them ok?
#we want that in our language ! and say 0 be false and 1 be true !
#and is both are true abd or is any one statement is true !

TT_EQEQ = 'TT_EQEQ' # ==
TT_NE = 'TT_NE' #!=
TT_LT = 'TT_LT' #< (lower than)
TT_GT = 'TT_GT' #> (greater than)
TT_LTE = 'TT_LTE' #<= (lower_than_equal to 0
TT_GTE = 'TT_GTE'

TT_AND = 'TT_AND' # &&
TT_OR = 'TT_OR' # ||
TT_NOT = 'TT_NOT' # !

#Custom Functions of my language
TT_POW='POW'
TT_SQRT='SQRT'
TT_CUBE='CUBE'
TT_EVEN_CHECK='EVEN_CHECK'
TT_ODD_CHECK='ODD_CHECK'
TT_ABS='ABS'

#get the string letters ! yeah?

LETTERS=string.ascii_letters
LETTERS_DIGITS=LETTERS+DIGITS




class Token: #dope class token love token give meee
    def __init__(self, type_, value=None, line=None, column=None):
        self.type = type_
        self.value = value
        self.line = line
        self.column = column

    def __repr__(self):
        if self.value is not None:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

    def matches(self,type_,value):
        return self.type ==type_ and self.value==value




#########
# Errors we all love errors mate huh ?who the am i talking to>?CIA >>???Terry Davis lol ><
#########

class Error(Exception):
    def __init__(self, error_name, details, line, column):
        super().__init__(details)

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
            "Illegal Character", #hey it is illegal mate
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


####Making of the RunTime  error of the value so that we can make the RunTime error of the runTime error

class RunTimeError(Error):
    def __init__(self, details, line, column):
        super().__init__(
            "Run Time Error",
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

                tokens.append(
                    Token(
                        TT_PLUS,
                        '+',
                        self.line,
                        self.column
                    )
                )

                self.advance()

            elif self.curr == '-':

                tokens.append(
                    Token(
                        TT_MINUS,
                        '-',
                        self.line,
                        self.column
                    )
                )

                self.advance()

            elif self.curr == '*':

                tokens.append(
                    Token(
                        TT_MUL,
                        '*',
                        self.line,
                        self.column
                    )
                )

                self.advance()

            elif self.curr == '/':

                tokens.append(
                    Token(
                        TT_DIV,
                        '/',
                        self.line,
                        self.column
                    )
                )

                self.advance()

            elif self.curr == '(':

                tokens.append(
                    Token(
                        TT_LPAREN,
                        '(',
                        self.line,
                        self.column
                    )
                )

                self.advance()

            elif self.curr == ')':

                tokens.append(
                    Token(
                        TT_RPAREN,
                        ')',
                        self.line,
                        self.column
                    )
                )

                self.advance()

            elif self.curr in DIGITS:

                tokens.append(
                    self.make_numbers_lol()
                )

            elif self.curr == '^':

                tokens.append(
                    Token(
                        TT_POW,
                        '^',
                        self.line,
                        self.column
                    )
                )

                self.advance()

            elif self.curr == '=': #so we are getting the eqaul for making v <variable_name> = <expr>/<value>ok?
                #this one also checks for == now so only ONE = branch lives here
                tokens.append(self.make_equals())

            elif self.curr =='!':
                tok,error=self.make_not_equals() #get the ! equal function of it !
                if error:return [],[error]
                tokens.append(tok)

            elif self.curr == '>': #so we are getting the >= one
                tokens.append(self.make_more_than())

            elif self.curr == '<': #so we are getting the <= one
                tokens.append(self.make_less_than())

            elif self.curr in LETTERS + '_':

                start_line = self.line
                start_column = self.column

                #make_identifier reads the whole word for us (letters digits and _)
                id_token = self.make_identifier()
                word = id_token.value

                if word == 'cube': #hell nah for cubes we loves cube a^3

                    tokens.append(
                        Token(
                            TT_CUBE,
                            'cube',
                            start_line,
                            start_column
                        )
                    )

                elif word == 'sqrt': #this one is for the sqrt ok ?

                    tokens.append(
                        Token(
                            TT_SQRT,
                            'sqrt',
                            start_line,
                            start_column
                        )
                    )

                elif word == 'even_check': #here it is the token to make a custom check for my program of even number

                    tokens.append(
                        Token(
                            TT_EVEN_CHECK,
                            'even_check',
                            start_line,
                            start_column
                        )
                    )

                elif word =="SRI": #It is getting tthe token about my cute little girl
                    tokens.append(
                        Token(
                            TT_SRI,
                            "SRI",
                            start_line,
                            start_column
                        )
                    )

                elif word=='odd_check': #i love to do the alternate ones bro that is why ODD baby

                    tokens.append(
                        Token(
                            TT_ODD_CHECK,
                            "odd_check",
                            start_line,
                            start_column
                        )
                    )

                elif word == 'abs': #absolute value of it and it means positive to be positive and negative to be positive

                    tokens.append(
                        Token(
                            TT_ABS,
                            'abs',
                            start_line,
                            start_column
                        )
                    )

                else:

                    #not one of our custom words so it is a keyword (V) or a variable name
                    tokens.append(id_token)

            else:

                errors.append(
                    IllegalCharError(
                        f"'{self.curr}'",
                        self.line,
                        self.column
                    )
                )

                self.advance()

        tokens.append(Token(TT_EOF, None, self.line, self.column + 1))

        return tokens, errors

    def make_numbers_lol(self):

        num_str = ''
        dot_count = 0

        start_line = self.line
        start_column = self.column

        while self.curr != None and self.curr in DIGITS + '.':

            if self.curr == '.':

                if dot_count == 1:
                    break

                dot_count += 1

            num_str += self.curr

            self.advance()

        if dot_count == 0:

            return Token(
                TT_INT,
                int(num_str),
                start_line,
                start_column
            )

        return Token(
            TT_FLOAT,
            float(num_str),
            start_line,
            start_column
        )

    def make_equals(self):
        #so we are getting the == one function over here ! (single = stays TT_EQ for variables)
        line, col = self.line, self.column
        self.advance()

        if self.curr == '=':
            self.advance()
            return Token(TT_EQEQ, '==', line, col)

        return Token(TT_EQ, '=', line, col)

    def make_not_equals(self):
        line, col = self.line, self.column
        self.advance()

        if self.curr == '=':
            self.advance()
            return Token(TT_NE, '!=', line, col), None #the second part is for the error ok ?

        return None, InvalidSyntaxError("Expected '=' after '!'", line, col) #now it is a real Error object so run() can print it !

    def make_less_than(self):
        line, col = self.line, self.column #so we are getting the <= one function over here !
        self.advance()

        if self.curr == '=': #so checking it and calling the = function !
            self.advance()
            return Token(TT_LTE, '<=', line, col)

        return Token(TT_LT, '<', line, col)

    def make_more_than(self):
        line, col = self.line, self.column #so we are getting the >= one function over here !
        self.advance()

        if self.curr == '=': #so checking it and calling the = function !
            self.advance()
            return Token(TT_GTE, '>=', line, col)

        return Token(TT_GT, '>', line, col)




    def make_identifier(self):
        id_start='' #getting the start of it ?
        start_line=self.line
        start_column=self.column
        while self.curr !=None and self.curr in LETTERS_DIGITS +'_':
            #so we are trying that our character should not be null and should have letters and dgits in it
            id_start=id_start+self.curr
            self.advance()

        tok_type=TT_KEYWORD if id_start in  KEYWORDS else TT_IDENTIFIER
        return  Token(tok_type,id_start,start_line,start_column)



##########################
# NODES
##########################
#we neeed the for loop and the while loop in my lang so lol i am gonna make it yeah
#tmy project is getting kinda cool I AM LOVING it i am getting to YOU Terry Davis

class ForNode:
    def __init__(self,var_name,start_token,end_value_Node,step_value,Body_Node):
        #takign all of these vals lol !
        self.var_name=var_name
        self.start_token=start_token
        self.end_value_Node=end_value_Node
        self.step_value=step_value
        self.Body_Node=Body_Node
class WhileNode: #getting the values for the while lOOp yeahhh !
    def __init__(self,condition_Node,body_Node):
        self.condition_Node=condition_Node
        self.body_Node=body_Node

class PrintNode:
    def __init__(self,node):
        self.node=node

    def __repr__(self):
        return f'(print {self.node})'


class IfNode:
    def __init__(self,cases,else_case):
        self.cases=cases
        self.else_case=else_case #getting thr if part and the else part of it !

    def __repr__(self):
        return f'(if {self.cases} else {self.else_case})' #return th value expression that we are getting !


class NumberNodes:  # Hey lol so this is for th Numbers in our language

    def __init__(self, tok):
        self.tok = tok

    def __repr__(self):
        return f'{self.tok}'

class VariableAccessNode:
    def __init__(self,var_name):
        self.var_name=var_name

        self.line=self.var_name.line
        self.column=self.var_name.column

    def __repr__(self):
        return f'(get {self.var_name.value})'


class VariableAssignNode:
    def __init__(self,var_name,value_node):
        self.var_name=var_name
        self.value_node=value_node

        self.line=self.var_name.line
        self.column=self.var_name.column

    def __repr__(self):
        return f'(set {self.var_name.value} = {self.value_node})'


class BinOp:  # and this is for the binary ops such as 1+2 like this !!

    def __init__(self, left_node, op_token, right_node):
        self.left_node = left_node
        self.op_token = op_token
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node} {self.op_token} {self.right_node})'


class UnaryOp:

    def __init__(self, op_token, node):
        self.op_token = op_token
        self.node = node

    def __repr__(self):
        return f'({self.op_token}{self.node})'


class EvenCheckForReal:

    def __init__(self,node,line=None,column=None):
        self.node=node
        self.line=line
        self.column=column

    def __repr__(self):
        return f'[Even Baby]{self.node}'


class OddCheckForReal:

    def __init__(self,node,line=None,column=None):
        self.node=node
        self.line=line
        self.column=column

    def __repr__(self):
        return f'[Odd Baby]{self.node}'


class SriForReal: #it is the class name about my cute little girl and i love her !
    def __init__(self,node):
        self.node=node
    def __repr__(self):
        return f'[Sri my Cutie Little princess]{self.node}'

class AbsForReal:

    def __init__(self,node):
        self.node=node

    def __repr__(self):
        return f'[Absolute Baby]{self.node}'


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

    def atom(self):

        res = ParserResult()

        tok = self.current_tok

        if tok.matches(TT_KEYWORD,"IF"):
            return self.if_expr() #parsing it in my parser and getting the if staemtnt out of ut !

        if tok.matches(TT_KEYWORD,"print") or tok.matches(TT_KEYWORD,"PRINT"):
            self.advance()

            value = res.registers(self.expr())

            if res.error:
                return res

            return res.success(PrintNode(value.node))


        if tok.type == TT_IDENTIFIER:
            self.advance()
            return res.success(VariableAccessNode(tok))

        if tok.type in (TT_INT, TT_FLOAT):

            self.advance()

            return res.success(
                NumberNodes(tok)
            )
        #getting the token of the for and the while loop

        if tok.matches(TT_KEYWORD,'FOR'):
            return self.for_expr() #callin our for_expr() function

        if tok.matches(TT_KEYWORD,'WHILE'):
            return self.while_expr() #getting the while_expr() function


        if tok.type == TT_LPAREN:

            self.advance()

            expr = res.registers(
                self.expr()
            )


            if res.error:
                return res

            if self.current_tok.type == TT_RPAREN:

                self.advance()

                return res.success(expr.node)

            return res.failure(
                InvalidSyntaxError(
                    "Expected ')'",
                    self.current_tok.line,
                    self.current_tok.column
                )
            )


        return res.failure(
            InvalidSyntaxError(
                "Expected number, variable, print, if, for, while or '('",
                tok.line,
                tok.column
            )
        )

    def if_expr(self):
        res = ParserResult()
        cases = []
        else_case = None

        self.advance() #skip the IF staatemnt !


        condition = res.registers(self.expr())
        if res.error: return res

        if not self.current_tok.matches(TT_KEYWORD, "THEN"):
            return res.failure(
                InvalidSyntaxError("Expected 'THEN'", self.current_tok.line, self.current_tok.column)
            )

        self.advance() #skip the THEN

        body = res.registers(self.expr())
        if res.error: return res

        cases.append((condition.node, body.node))

        while self.current_tok.matches(TT_KEYWORD, "ELIF"):

            self.advance() #skip the ELIF

            condition = res.registers(self.expr())
            if res.error: return res

            if not self.current_tok.matches(TT_KEYWORD, "THEN"):
                return res.failure(
                    InvalidSyntaxError("Expected 'THEN'", self.current_tok.line, self.current_tok.column)
                )

            self.advance()

            body = res.registers(self.expr())
            if res.error: return res

            cases.append((condition.node, body.node))

        if self.current_tok.matches(TT_KEYWORD, "ELSE"):

            self.advance() #skip the ELSE

            else_body = res.registers(self.expr())
            if res.error: return res

            else_case = else_body.node

        return res.success(IfNode(cases, else_case))
    def for_expr(self):
        res=ParserResult()

        #if it does not matches with the for keyword then we can say its an error
        if not self.current_tok.matches(TT_KEYWORD,"FOR"):
            return res.failure(
                InvalidSyntaxError(
                    "WE NEED THE FOR KEYWORD",
                    self.current_tok.line,
                    self.current_tok.column
                )
            )

        self.advance()

        if self.current_tok.type!=TT_IDENTIFIER:
            return res.failure(
                InvalidSyntaxError(
                    "WE NEED AN IDENTIFIER",
                    self.current_tok.line,
                    self.current_tok.column
                )
            )

        var_name=self.current_tok
        self.advance()

        #then we have to look for the equal tokens in our code base i=1 to 10 something like this that i am thinking!

        if self.current_tok.type!=TT_EQ: #if the person misses = symbpol in the code base fr example i 1 to 10

            return res.failure(
                InvalidSyntaxError(
                    "MISSING = sign correct your syntax !",
                    self.current_tok.line,
                    self.current_tok.column
                )
            )

        self.advance()

        #get the start value of the expression !

        start_value=res.registers(self.expr()) #get tje starting <oh no > repetation !
        if res.error:return res

        if not self.current_tok.matches(TT_KEYWORD,"TO"):
            return res.failure(
                InvalidSyntaxError(
                    "MISSING THE =>TO<= KEYWORD!",
                    self.current_tok.line,
                    self.current_tok.column
                )
            )

        self.advance()

        end_value=res.registers(self.expr())
        if res.error:return res

        if not self.current_tok.matches(TT_KEYWORD,"THEN"):
            return res.failure(
                InvalidSyntaxError(
                    "MISSING THE =>THEN<= KEYWORD!",
                    self.current_tok.line,
                    self.current_tok.column
                )
            )

        self.advance()

        body=res.registers(self.expr())
        if res.error:return res

        return res.success(
            ForNode(
                var_name,
                start_value.node,
                end_value.node,
                1,
                body.node
            )
        )

    def while_expr(self):
        res=ParserResult()

        #getting the values for the while loop yeahhh !
        if not self.current_tok.matches(TT_KEYWORD,"WHILE"):
            return res.failure(
                InvalidSyntaxError(
                    "WE NEED THE WHILE KEYWORD",
                    self.current_tok.line,
                    self.current_tok.column
                )
            )

        self.advance()

        condition=res.registers(self.expr())
        if res.error:return res

        if not self.current_tok.matches(TT_KEYWORD,"THEN"):
            return res.failure(
                InvalidSyntaxError(
                    "MISSING THE =>THEN<= KEYWORD!",
                    self.current_tok.line,
                    self.current_tok.column
                )
            )

        self.advance()

        body=res.registers(self.expr())
        if res.error:return res

        return res.success(
            WhileNode(
                condition.node,
                body.node
            )
        )

    def cubeatom(self):

        res = ParserResult()

        left = res.registers(
            self.power()
        )

        if res.error:
            return res

        left = left.node

        while self.current_tok.type == TT_CUBE:

            op_tok = self.current_tok

            self.advance()

            #UnaryOp so the inside gets evaluated only ONE time (a * a * a in the interpreter)
            left = UnaryOp(
                op_tok,
                left
            )

        return res.success(left)

    def power(self):

        #right side is a factor now so 2^-1 works (and 2^3^2 is 2^(3^2) like normal maths)
        res = ParserResult()

        left = res.registers(
            self.atom()
        )

        if res.error:
            return res

        left = left.node

        if self.current_tok.type == TT_POW:

            op_tok = self.current_tok

            self.advance()

            right = res.registers(
                self.factor()
            )

            if res.error:
                return res

            left = BinOp(
                left,
                op_tok,
                right.node
            )

        return res.success(left)

    def factor(self):

        res = ParserResult()

        tok = self.current_tok

        if tok.type in (TT_PLUS, TT_MINUS):

            self.advance()

            factor = res.registers(
                self.factor()
            )

            if res.error:
                return res

            return res.success(
                UnaryOp(
                    tok,
                    factor.node
                )
            )

        if tok.type == TT_SQRT:

            self.advance()

            number = res.registers(
                self.factor()
            )

            if res.error:
                return res

            return res.success(
                BinOp(
                    number.node,
                    Token(
                        TT_POW,
                        '^',
                        tok.line,
                        tok.column
                    ),
                    NumberNodes(
                        Token(
                            TT_FLOAT,
                            0.5,
                            tok.line,
                            tok.column
                        )
                    )
                )
            )

        if tok.type == TT_EVEN_CHECK:

            self.advance()

            number = res.registers(
                self.factor()
            )

            if res.error:
                return res

            return res.success(
                EvenCheckForReal(
                    number.node,
                    tok.line,
                    tok.column
                )
            )

        if tok.type == TT_ODD_CHECK:

            self.advance()

            number = res.registers(
                self.factor()
            )

            if res.error:
                return res

            return res.success(
                OddCheckForReal(
                    number.node,
                    tok.line,
                    tok.column
                )
            )

        if tok.type == TT_ABS:

            self.advance()

            number = res.registers(
                self.factor()
            )

            if res.error:
                return res

            return res.success(
                AbsForReal(
                    number.node
                )
            )

        if tok.type == TT_SRI: #my cute little girl lives in factor like abs does

            self.advance()

            number = res.registers(
                self.factor()
            )

            if res.error:
                return res

            return res.success(
                SriForReal(
                    number.node
                )
            )

        return self.cubeatom()

    def bin_op(self, func, ops):

        res = ParserResult()

        left = res.registers(func())

        if res.error:
            return res

        left = left.node

        #ops can hold plain token types (TT_PLUS) OR (type, value) pairs like (TT_KEYWORD, "AND")
        while (self.current_tok.type in ops or
               (self.current_tok.type, self.current_tok.value) in ops):

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

    def arith_expr(self):

        #the old + and - level lives here now
        return self.bin_op(
            self.term,
            (TT_PLUS, TT_MINUS)
        )


    def comp_expr(self):

        #NOT comp_expr  OR  arith_expr ((== != < > <= >=) arith_expr)*
        res = ParserResult()

        if self.current_tok.matches(TT_KEYWORD, "NOT"):

            op_tok = self.current_tok

            self.advance()

            node = res.registers(
                self.comp_expr()
            )

            if res.error:
                return res

            return res.success(
                UnaryOp(
                    op_tok,
                    node.node
                )
            )

        return self.bin_op(
            self.arith_expr,
            (TT_EQEQ, TT_NE, TT_LT, TT_GT, TT_LTE, TT_GTE)
        )

    def expr(self):

        res = ParserResult()

        if self.current_tok.matches(TT_KEYWORD,"V"):
            res.registers(self.advance()) #getting the adnave one so that we can go to the next one
            #check for the name of our variable !@!
            if self.current_tok.type !=TT_IDENTIFIER:
                return res.failure(
                    InvalidSyntaxError(
                        "Hey homie you dumb cuz you know what you JUST GAVE YOUR code an ERROR as variable name cannot have the same name of the identifier godd damn it",
                        self.current_tok.line,
                        self.current_tok.column
                    )
                )
            var_name= self.current_tok
            res.registers(self.advance()) #go for the next one

            #now we have to get the = one to have a normal expression of it

            if self.current_tok.type !=TT_EQ:
                return res.failure(
                    InvalidSyntaxError(
                        "FORGOT THE = SYMBOL IDIOIT ! I AM ANGRY WITH YA ",
                        self.current_tok.line,
                        self.current_tok.column
                    )
                )
            res.registers(self.advance())
            expr=res.registers(self.expr())
            if res.error:return res
            return res.success(VariableAssignNode(var_name,expr.node))


        #AND / OR sit on top of the comparisons
        return self.bin_op(
            self.comp_expr,
            ((TT_KEYWORD, "AND"), (TT_KEYWORD, "OR"))
        )

    ## Parse Function to join them

    def parse(self):

        res = self.expr()

        if res.error:
            return res

        if self.current_tok.type != TT_EOF:

            return res.failure(
                InvalidSyntaxError(
                    "Expected '+', '-', '*', '/', '^', 'cube', comparison, 'AND', 'OR' or end of expression",
                    self.current_tok.line,
                    self.current_tok.column
                )
            )

        return res


##########################
# SYMBOL TABLE (remembers our V variables)
##########################

class SymbolTable:

    def __init__(self):

        self.symbols = {}

    def get(self, name):

        return self.symbols.get(name)

    def has(self, name):

        return name in self.symbols

    def set(self, name, value):

        self.symbols[name] = value


##########################
# INTERPRETER MAKING OF IT
##########################

class Interpreter:

    def __init__(self, symbol_table):

        self.symbol_table = symbol_table

    def visit(self, node):

        method_name = f'visit{type(node).__name__}'

        method = getattr(
            self,
            method_name,
            self.no_visit_method
        )

        return method(node)

    def no_visit_method(self, node):

        raise Exception(
            f'No visit{type(node).__name__} method defined!'
        )

    def visitNumberNodes(self, node):

        return node.tok.value

    def visitVariableAccessNode(self, node):

        name = node.var_name.value

        if not self.symbol_table.has(name):

            raise RunTimeError(
                f"'{name}' is not defined",
                node.line,
                node.column
            )

        return self.symbol_table.get(name)

    def visitVariableAssignNode(self, node):

        name = node.var_name.value

        value = self.visit(node.value_node)

        self.symbol_table.set(name, value)

        return value

    def visitIfNode(self, node):

        for condition, body in node.cases:

            if self.visit(condition): #anything not 0 is true
                return self.visit(body)

        if node.else_case is not None:
            return self.visit(node.else_case)

        return 0 #no case matched and no ELSE

    def visitPrintNode(self, node):

        value = self.visit(node.node)

        print(value)

        return None

    def visitForNode(self, node):

        start_value = self.visit(node.start_token)
        end_value = self.visit(node.end_value_Node)

        current = int(start_value)
        end_value = int(end_value)
        result = None

        while current <= end_value:

            self.symbol_table.set(node.var_name.value, current)

            result = self.visit(node.Body_Node)

            current += node.step_value

        return result

    def visitWhileNode(self, node):

        result = None

        while self.visit(node.condition_Node):

            result = self.visit(node.body_Node)

        return result

    def whole_number(self, number, line, column):

        #even/odd only make sense for whole numbers (2.0 is ok, 2.5 is not)
        if isinstance(number, float) and not number.is_integer():

            raise RunTimeError(
                "even_check/odd_check need a whole number",
                line,
                column
            )

        return int(number)

    def visitEvenCheckForReal(self, node):

        number = self.visit(node.node)

        number = self.whole_number(number, node.line, node.column)

        return int(number % 2 == 0) #1 for true 0 for false !

    def visitOddCheckForReal(self, node):

        number = self.visit(node.node)

        number = self.whole_number(number, node.line, node.column)

        return int(number % 2 != 0) #1 for true 0 for false !

    def visitAbsForReal(self, node):

        number = self.visit(node.node)

        return abs(number)

    def visitSriForReal(self, node):

        number = self.visit(node.node)

        return number * 2 #love doubles everything and i really love you and that si what i am doing it !

    def visitBinOp(self, node):

        left = self.visit(node.left_node)
        right = self.visit(node.right_node)

        line = node.op_token.line
        column = node.op_token.column

        if node.op_token.type == TT_PLUS:

            return left + right

        elif node.op_token.type == TT_MINUS:

            return left - right

        elif node.op_token.type == TT_MUL:

            return left * right

        elif node.op_token.type == TT_DIV:

            if right == 0:
                raise RunTimeError(
                    "Are u dumb to divide by 0?bro?hell nah >< It is an ERROR ",
                    line,
                    column
                )

            try:
                return left / right
            except OverflowError:
                raise RunTimeError("Result is too big", line, column)

        #relational ones (1 is true and 0 is false)
        elif node.op_token.type == TT_EQEQ: return int(left == right)
        elif node.op_token.type == TT_NE:   return int(left != right)
        elif node.op_token.type == TT_LT:   return int(left < right)
        elif node.op_token.type == TT_GT:   return int(left > right)
        elif node.op_token.type == TT_LTE:  return int(left <= right)
        elif node.op_token.type == TT_GTE:  return int(left >= right)

        #conditional ones
        elif node.op_token.matches(TT_KEYWORD, "AND"): return int(bool(left) and bool(right))
        elif node.op_token.matches(TT_KEYWORD, "OR"):  return int(bool(left) or bool(right))

        elif node.op_token.type == TT_POW:

            try:
                answer = left ** right
            except ZeroDivisionError:
                raise RunTimeError("0 cannot be raised to a negative power", line, column)
            except OverflowError:
                raise RunTimeError("Result is too big", line, column)

            if isinstance(answer, complex):
                raise RunTimeError(
                    "Cannot take sqrt/fractional power of a negative number",
                    line,
                    column
                )

            return answer

    def visitUnaryOp(self, node):

        number = self.visit(node.node)

        t = node.op_token

        if t.type == TT_MINUS:

            return -number

        elif t.type == TT_PLUS:

            return number

        elif t.type == TT_CUBE:

            return number * number * number

        elif t.matches(TT_KEYWORD, "NOT"):

            return int(not number)


##########################
# RUN
##########################

global_symbol_table = SymbolTable() #lives forever so variables stay alive between lines

def run(text):

    lexer = Lexer(text)

    tokens, errors = lexer.lets_cook_tokens()

    if errors:
        return None, errors

    # MAKING OF AST

    parser = Parser(tokens)

    ast = parser.parse()

    if ast.error:
        return None, [ast.error]

    # CHECK THE INTERPRETER FOR ME LOL

    interpreter = Interpreter(global_symbol_table)

    try:

        result = interpreter.visit(ast.node)

        return result, None

    except RunTimeError as error:

        return None, [error]

    except Exception as error: #anything else so the REPL never dies

        return None, [RunTimeError(str(error), 0, 0)]


##########################
# TERMINAL
##########################
def run_file(filename):

    if not filename.endswith(".prax"):
        print("PraxLang files must end with .prax")
        return

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"File '{filename}' not found")
        return

    for file_line, line in enumerate(lines, start=1):

        if line.strip() == "":
            continue

        result, errors = run(line)

        if errors:
            for error in errors:
                print(
                    f"\033[91m[ERROR]\033[0m "
                    f"{error.as_String()} "
                    f"[{filename}, file line {file_line}]"
                )
            return #stop at the first error

        if result is not None:
            print(result)

#making a function so that i can have my own extenstion !
def repl():

    while True:

        try:
            text = input("PraxLang >>> ")
        except (EOFError, KeyboardInterrupt):
            print("\nBye 👋 users !! it is a cruel world a cruel language i am making !")
            break

        if text.strip() == "":
            continue

        if text == "exit":

            print("Bye 👋 and yahh the programming language of mine is dopw ")

            break

        result, errors = run(text)

        if errors:

            for error in errors:

                print(
                    f"\033[91m[ERROR]\033[0m "
                    f"{error.as_String()}"
                )

        else:

            if result is not None:
                print(
                    f"\033[92m[RESULT]\033[0m "
                    f"{result}"
                )


if __name__ == "__main__":

    if len(sys.argv) > 1:
        run_file(sys.argv[1]) #python praxlang.py myfile.prax
    else:
        repl() #python praxlang.py of the language of it !


#hey we want some variables in this good damn langauge lol ???

#so  see i dont want it to name it like var <varable name> = <expr>  {NO JS LIKE PLS SORRY }

#so name it LIKE V (CyberPunk 2077 ) lol v <variable name>=<expr>  {so it is like 2077 not some agentic bs<> so do it the part i am doing !
