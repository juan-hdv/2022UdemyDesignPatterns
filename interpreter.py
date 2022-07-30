"""
Interpreter Coding Exercise

You are asked to write an expression processor for simple numeric expressions
with the following constraints:

Expressions use integral values (e.g., '13' ),
single-letter variables defined in Variables, as well as + and - operators only

There is no need to support braces or any other operations

If a variable is not found in variables
(or if we encounter a variable with >1 letter, e.g. ab),
the evaluator returns 0 (zero)

In case of any parsing failure, evaluator returns 0

Example:

calculate("1+2+3")  should return 6

calculate("1+2+xy")  should return 0

calculate("10-2-x")  when x=3 is in variables  should return 5
"""


class Tokenizer:
    def __init__(self, expression) -> None:
        self.tokens = []
        self.expression = expression
        self.success = True

    class Type:
        INT = 1
        VAR = 2
        PLUS_SIGN = 3
        MINUS_SIGN = 4

    class Token:
        def __init__(self, type, repr) -> None:
            self.type = type
            self.repr = repr

    def lex(self):
        k = 0
        while k < len(self.expression) and self.success:
            if self.expression[k] == " ":
                k += 1
                continue
            if self.expression[k].isnumeric():
                string = ""
                while k < len(self.expression) and self.expression[k].isnumeric():
                    string += self.expression[k]
                    k += 1
                self.tokens.append(self.Token(self.Type.INT, string))
            elif self.expression[k].isalpha():
                string = ""
                while k < len(self.expression) and self.expression[k].isalpha():
                    string += self.expression[k]
                    k += 1
                self.tokens .append(self.Token(self.Type.VAR, string))
            elif self.expression[k] == "+":
                self.tokens .append(self.Token(self.Type.PLUS_SIGN, self.expression[k]))
                k += 1
            elif self.expression[k] == "-":
                self.tokens .append(self.Token(self.Type.MINUS_SIGN, self.expression[k]))
                k += 1
            else:
                self.success = False

        return self.success

    def __str__(self) -> str:
        return f"Success ({self.success}) - Tokens: {[(t.type,t.repr) for t in self.tokens]}"


class Parser:
    def __init__(self, tokens, variables) -> None:
        self.tokens = tokens
        self.variables = variables
        self.evaluation_string = ""

    def parse(self) -> bool:
        k = 0
        if self.tokens[k].type not in (Tokenizer.Type.INT, Tokenizer.Type.VAR):
            return ""

        result = ""
        correct_gramar = True
        token = self.tokens[k]

        while k < len(self.tokens) and correct_gramar:
            token = self.tokens[k]
            if token.type in (Tokenizer.Type.INT, Tokenizer.Type.VAR):
                if (k+1 < len(self.tokens) and
                    self.tokens[k+1].type not in (
                        Tokenizer.Type.PLUS_SIGN,
                        Tokenizer.Type.MINUS_SIGN
                    )
                ):
                    correct_gramar = False
                else:
                    result += str(
                        self.variables.get(token.repr, 0)
                        if  token.type == Tokenizer.Type.VAR else token.repr
                    )
            elif token.type in (Tokenizer.Type.PLUS_SIGN, Tokenizer.Type.MINUS_SIGN):
                if (k+1 < len(self.tokens) and
                    self.tokens[k+1].type not in (
                        Tokenizer.Type.INT,
                        Tokenizer.Type.VAR
                    )
                ):
                    correct_gramar = False
                else:
                    result += token.repr
            k += 1
        
        self.evaluation_string = result if correct_gramar else ""
        return correct_gramar

    def evaluate(self):
        if self.evaluation_string:
            return eval(self.evaluation_string)
        
        return 0 



class ExpressionProcessor:
    def __init__(self):
        self.variables = dict(
            a=1,
            b=2
        )

    def calculate(self, expression):
        tk = Tokenizer (expression)
        success = tk.lex()
        if not success:
            return "Error: Invalid expression. Lex failed"

        tokens = tk.tokens
        print (f"Tokens = {tk}")

        p = Parser (tokens, self.variables)
        if not p.parse():
            return "Error: Invalid expression - Pase failed"
        
        return p.evaluate()

e = ExpressionProcessor()
print ("Result: ", e.calculate("bb - aa - vvb")) 
