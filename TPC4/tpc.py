import re
import sys

def tokenize(code):
    token_specification = [
        ('KW_SELECT', r'select'),
        ('KW_WHERE', r'where'),
        ('KW_LIMIT', r'LIMIT'),
        ('VAR', r'\?[A-Za-z_][A-Za-z0-9_]*'),  # Variáveis começam com '?'
        ('PREFIX', r'dbo:|foaf:'),  # Prefixos conhecidos
        ('ID', r'[A-Za-z_][A-Za-z0-9_]*'),  # Identificadores genéricos (MusicalArtist, name, etc.)
        ('COMMENT', r'#.*'),  # Comentários iniciados por '#'
        ('STRING', r'"[^"]*"(@[a-z]+)?'),  # Strings com possível tag de linguagem
        ('NUM', r'\d+'),  # Números inteiros
        ('OP', r'[{}.:]'),  # Operadores e delimitadores
        ('WS', r'[ \t\n]+'),  # Espaços e quebras de linha
        ('ERRO', r'.'),  # Qualquer outro caractere inválido
    ]
    
    tok_regex = '|'.join(f'(?P<{name}>{pattern})' for name, pattern in token_specification)
    tokens = []
    
    for match in re.finditer(tok_regex, code, re.IGNORECASE):
        kind = match.lastgroup
        value = match.group()
        
        if kind in ['WS', 'COMMENT']: # se eu quiser ignorar os comentários apenas tenho de deixar COMMENT aqui
            continue
        elif kind == 'NUM':
            value = int(value)
        elif kind == 'STRING':
            value = value.strip('"')
        
        tokens.append((kind, value))
    
    return tokens

if __name__ == "__main__":
    code = sys.stdin.read()
    for token in tokenize(code):
        print(token)