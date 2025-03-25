import ply.yacc as yacc
import re
from tokens import tokens

# Definição da gramática
def p_expression_plus(p):
    'expression : expression PLUS term'
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS term'
    p[0] = {"currentexp":(p[1],p[3 ])}
    print(p[1] - p[3])

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES factor'
    p[0] = p[1] * p[3]

def p_term_div(p):
    'term : term DIVIDE factor'
    p[0] = p[1] / p[3]

def p_term_factor(p):
    'term : factor'
    p[0] = p[1]

def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]

def p_factor_expr(p):
    'factor : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Erro sintático no input!")

# expression : term
#           | expression PLUS term
#           | expression MINUS term
# term : term TIMES factor
#     |term DIVIDE factor
#     | factor
# factor : NUMBER
#        | LPAREN expression RPAREN


# Cria o parser
parser = yacc.yacc()

# Expressão regular para capturar palavras de saída
exit_regex = re.compile(r"^(exit|quit|q|sair|fechar)$", re.IGNORECASE)

# Loop para ler expressões do teclado
if __name__ == "__main__":
    while True:
        try:
            entrada = input("Escreve uma expressão: ")
        except EOFError: # End of file
            break
        if not entrada:
            continue
        if exit_regex.match(entrada):
            break
        resultado = parser.parse(entrada)
        print(f"Resultado: {resultado}")