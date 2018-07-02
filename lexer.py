import ply.lex as lex

#Nombre de lista de Token

tokens = ('QUOTE', 'SIMB', 'NUM', 'NAME','LPAREN', 'RPAREN', \
          'NIL', 'TRUE', 'FALSE', 'TEXT', 'PLUS', 'MINUS', 'DIVIDE')

#PALABRAS RESERVADAS
reserved = {'nil' : 'NIL'}

#EXPRESIONES REGULARES REGLAS PARA SIMPLE TOKENS
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_QUOTE = r'\''
t_TRUE = r'\#t'
t_FALSE = r'\#f'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PLUS = r'\+'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUM(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print "Line %d: Numero % es largo!" % (t.lineno, t .value)
        t.value = 0
        return t

def t_SIMB(t):
    r'[a-zA-Z_+=\*\-][a-zA-Z0-9_+\*\-]*'
    t.type = reserved.get(t.value, 'SIMB') # CHEQUEA PALABRAS RESERVADAS
    return t

def t_TEXT(t)
    r'\'[a-zA-Z0-9_+\*\- :,]*\''
    t.type = reserved.get(t.value, 'TEXT') #CHEQUEA LAS PALBRAS RESERVADAS
    return t

#IGNORANDO CARACTERES ESPACIOS Y TABS
t_ignore = '\t'

#ERROR
def t_error(t):
    print("Lexical: illegal character '%s' in line '%d' position" % (t.value[0], t.lineno))
    t.lexer.skip(1)

lex.lex()

if _name_ == '_main_':
    lex.runmain()
