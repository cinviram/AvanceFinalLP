import ply.lex as lex

#Nombre de lista de Token

#revisar cuales no usamos al final
tokens = ('QUOTE', 'STRING','NUM','ALFNUM','LPAREN', 'RPAREN',
          'NIL', 'T', 'NIL', 'TEXT', 'PLUS', 'MINUS', 'DIVIDE',
          'TIMES', 'MAX','MIN','APPEND','CONS', 'FIRST', 'REST',
          'SPACE', 'APPLY')


#EXPRESIONES REGULARES REGLAS PARA SIMPLE

#simbolos
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_QUOTE = r'\'' #apostrofe
t_SPACE = r'\n'

#valores de verdad
t_T = r'\#t'
t_NIL = r'\#f'

#operadores
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PLUS = r'\+'

#tipos atomo
t_ALFNUM = r'[\w]+'
t_STRING = r'[a-zA-Z]'
t_NUM = r' [+-]?\d+(\.\d+|[eE][+-]?\d+)?'

#palabras reservadas
t_MAX = r'MAX'
t_MIN = r'MIN'
t_CONS = r'CONS'
t_APPEND = r'APPEND'
t_FIRST = r'FIRST'
t_REST = r'REST'
t_APPLY = r'APPLY'


#IGNORANDO CARACTERES ESPACIOS Y TABS
t_ignore = '\t'

#ERROR
def t_error(t):
    print("Lexical: illegal character '%s' in line '%d' position" % (t.value[0], t.lineno))
    t.lexer.skip(1)

lex.lex()


# MAIN
if __name__ == "__main__":
    print("Ingrese una palabra reservada , un operador o una variable de LISP : ")
    cadena=input()
    lex.input(cadena)

    while 1:
        token = lex.token()
        if not token:
            print("¡No es un token válido!")
            break
        print("Token valido de tipo : " + token.type)
        break
