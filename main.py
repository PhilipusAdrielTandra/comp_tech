class ParseTreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class RecursiveCalculator:
    def __init__(self, input_tokens):
        self._tokens = input_tokens
        self._current_token = input_tokens[0]

    def evaluate_expression(self):
        result, parse_tree = self.calculate_term()
        while self._current_token in ('+', '-'):
            operator = self._current_token
            self.advance()
            term_value, term_tree = self.calculate_term()
            if operator == '+':
                result += term_value
                parse_tree = ParseTreeNode("+", parse_tree, term_tree)
            elif operator == '-':
                result -= term_value
                parse_tree = ParseTreeNode("-", parse_tree, term_tree)
        return result, parse_tree

    def calculate_factor(self):
        result, parse_tree = None, None
        if self._current_token is None:
            raise ValueError("Unexpected end of input")
        if self._current_token[0].isdigit() or self._current_token[-1].isdigit():
            result = float(self._current_token)
            parse_tree = ParseTreeNode(result)
            self.advance()
        elif self._current_token == '(':
            self.advance()
            result, parse_tree = self.evaluate_expression()
            if self._current_token != ')':
                raise ValueError("Expected closing parenthesis ')'")
            self.advance()
        else:
            raise ValueError("Invalid input token: " + self._current_token)
        return result, parse_tree

    def advance(self):
        self._tokens = self._tokens[1:]
        self._current_token = self._tokens[0] if len(self._tokens) > 0 else None

    def calculate_term(self):
        result, parse_tree = self.calculate_factor()
        while self._current_token in ('*', '/'):
            operator = self._current_token
            self.advance()
            factor_value, factor_tree = self.calculate_factor()
            if operator == '*':
                result *= factor_value
                parse_tree = ParseTreeNode("*", parse_tree, factor_tree)
            elif operator == '/':
                if factor_value == 0:
                    raise ValueError("Division by zero is not allowed")
                result /= factor_value
                parse_tree = ParseTreeNode("/", parse_tree, factor_tree)
        return result, parse_tree

    def print_parse_tree(self, node, indent=""):
        if node is not None:
            print(indent + str(node.value))
            if node.left:
                self.print_parse_tree(node.left, indent + "  ")
            if node.right:
                self.print_parse_tree(node.right, indent + "  ")

if __name__ == '__main__':
    while True:
        user_input = list(input('> ').replace(' ', ''))
        input_tokens = []
        for i in range(len(user_input)):
            if user_input[i].isdigit() and i > 0 and (input_tokens[-1].isdigit() or input_tokens[-1][-1] == '.'):
                input_tokens[-1] += user_input[i]
            elif user_input[i] == '.' and i > 0 and input_tokens[-1].isdigit():
                input_tokens[-1] += user_input[i]
            else:
                input_tokens.append(user_input[i])
        
        try:
            calculator = RecursiveCalculator(input_tokens)
            result, parse_tree = calculator.evaluate_expression()
            print("Parse Tree:")
            calculator.print_parse_tree(parse_tree)
            print("Result:", result)
        except ValueError as e:
            print("Error:", e)
