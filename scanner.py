import os
import ply.lex as lex

# List of tokens
tokens = [
    'IDENTIFIER',
    'NUMBER',
    'STRING',
    'CHAR',
    'OPERATOR',
    'HASH',
    'LBRACE',
    'RBRACE',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'LBRACKET',
    'RBRACKET',
    'COMMA',
    'DOT',
]

# Reserved keywords
reserved = {
    'if': 'IF',
    'for': 'FOR',
    'while': 'WHILE',
    'include': 'INCLUDE',
}

# Add reserved keywords to tokens
tokens += list(reserved.values())

# Token definitions
t_ignore = ' \t'  # Skip spaces and tabs
t_OPERATOR = r'(>>|<<|[+\-*/=<>!&|]{1,2})'  # Include multi-character operators
t_STRING = r'\"([^\\\n]|(\\.))*?\"'  # Strings
t_CHAR = r'\'([^\\\n]|(\\.))*?\''  # Single-character literals
t_HASH = r'\#'  # Preprocessor directives
t_LBRACE = r'\{'  # Left brace
t_RBRACE = r'\}'  # Right brace
t_LPAREN = r'\('  # Left parenthesis
t_RPAREN = r'\)'  # Right parenthesis
t_SEMICOLON = r';'  # Semicolon
t_LBRACKET = r'\['  # Left bracket
t_RBRACKET = r'\]'  # Right bracket
t_COMMA = r','  # Comma

# Add a rule for dot (used in member access or floats)
def t_DOT(t):
    r'\.'
    return t

# Rules for identifiers
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')  # Check for reserved keywords
    return t

# Rules for numbers (integer and floating-point)
def t_NUMBER(t):
    r'\d+(\.\d+)?'  # Match integers and floats
    t.value = float(t.value) if '.' in t.value else int(t.value)
    return t

# Track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling for illegal characters
def t_error(t):
    print(f"Illegal character '{t.value[0]}' at line {t.lineno}")
    t.lexer.skip(1)

# Build lexer
lexer = lex.lex()

# Vulnerabilities to detect
vulnerabilities = {
    'cin': 'Potential unchecked input vulnerability.',
    'strcpy': 'Potential buffer overflow vulnerability.',
    'strcat': 'Potential buffer overflow vulnerability.',
    'gets': 'Unsafe function usage.',
    'password': 'Hardcoded credential detected.',
    'system': 'Command injection vulnerability.',
    'ifstream': 'Unchecked file handling vulnerability.',
    'malloc': 'Unchecked memory allocation vulnerability.',
    'rand': 'Insecure random number generation.',
    'nullptr': 'Potential null pointer dereference.',
    'free': 'Potential use-after-free vulnerability.',
    'new': 'Unchecked dynamic memory allocation vulnerability.',
    '+': 'Potential integer overflow/underflow.',
}

# Analyze the code
def analyze_code(code):
    lexer.input(code)
    results = []
    seen_tokens = set()  # Avoid duplicate vulnerability reporting

    while True:
        token = lexer.token()
        if not token:
            break

        if token.type == 'IDENTIFIER' and token.value in vulnerabilities:
            key = (token.lineno, token.value)
            if key not in seen_tokens:  # Avoid duplicates
                seen_tokens.add(key)
                results.append({
                    'line': token.lineno,
                    'vulnerability': vulnerabilities[token.value],
                    'token': token.value
                })
    return results

# Scan a file for vulnerabilities
def scan_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            code = file.read()
        return analyze_code(code)
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

if __name__ == "__main__":
    cpp_file = input("Enter the path to the C++ file: ")
    if cpp_file and os.path.exists(cpp_file):
        results = scan_file(cpp_file)
        if results:
            print("Vulnerabilities Found:")
            for result in results:
                print(f"Line {result['line']}: {result['vulnerability']} (Token: {result['token']})")
        else:
            print("No vulnerabilities found.")
    else:
        print("File not found.")

