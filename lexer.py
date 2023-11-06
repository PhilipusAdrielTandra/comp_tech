token_types = [
    ('assign', ':='),
    ('lparen', '('),
    ('rparen', ')'),
    ('plus', '+'),
    ('minus', '-'),
    ('times', '*'),
    ('div', '/'),
]

def is_digit(char):
    return '0' <= char <= '9'

def is_identifier_char(char):
    return 'a' <= char <= 'z' or 'A' <= char <= 'Z' or char == '_'

def tokenize(input_str):
    tokens = []
    i = 0
    while i < len(input_str):
        char = input_str[i]
        if char.isspace():
            i += 1
        elif char in "0123456789":
            start = i
            while i < len(input_str) and (is_digit(input_str[i]) or input_str[i] == '.'):
                i += 1
            value = input_str[start:i]
            tokens.append(('number', value))
        elif is_identifier_char(char):
            start = i
            while i < len(input_str) and (is_identifier_char(input_str[i]) or is_digit(input_str[i])):
                i += 1
            value = input_str[start:i]
            tokens.append(('id', value))
        elif char == '#':
            i += 1
            while i < len(input_str) and input_str[i] != '\n':
                i += 1
        else:
            found = False
            for token_type, pattern in token_types:
                if input_str[i:i + len(pattern)] == pattern:
                    tokens.append((token_type, pattern))
                    i += len(pattern)
                    found = True
                    break
            if not found:
                tokens.append(('error', char))
                i += 1

    return tokens

file_path = "calc.py"

try:
    with open(file_path, "r") as file:
        input_str = file.read()
except FileNotFoundError:
    print(f"File not found: {file_path}")
    exit(1)

tokens = tokenize(input_str)

for token_type, value in tokens:
    print(f"{token_type}: {value}")
