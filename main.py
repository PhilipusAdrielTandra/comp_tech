class RecursiveCalculator:
    def __init__(self, input_tokens):
        self._tokens = input_tokens
        self._current_token = input_tokens[0]

    def evaluate_expression(self):
        result = self.calculate_term()
        while self._current_token in ('+', '-'):
            if self._current_token == '+':
                self.advance()
                result += self.calculate_term()
            elif self._current_token == '-':
                self.advance()
                result -= self.calculate_term()
        return result

    def calculate_factor(self):
        result = None
        if self._current_token[0].isdigit() or self._current_token[-1].isdigit():
            result = float(self._current_token)
            self.advance()
        elif self._current_token == '(':
            self.advance()
            result = self.evaluate_expression()
            self.advance()
        return result

    def advance(self):
        self._tokens = self._tokens[1:]
        self._current_token = self._tokens[0] if len(self._tokens) > 0 else None

    def calculate_term(self):
        result = self.calculate_factor()
        while self._current_token in ('*', '/'):
            if self._current_token == '*':
                self.advance()
                result *= self.calculate_factor()
            elif self._current_token == '/':
                self.advance()
                result /= self.calculate_factor()
        return result

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
        print(RecursiveCalculator(input_tokens).evaluate_expression())
