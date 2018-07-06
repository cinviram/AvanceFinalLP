import ply.lex as lex

#Nombre de lista de Token

#revisar cuales no usamos al final

tokens = [
          #Simbolos
          'QUOTE', 'STRING','ALFNUM','LPAREN', 'RPAREN', 'LCOR', 'RCOR'
          #Operadores
          , 'PLUS', 'MINUS', 'DIVIDE','TIMES',
          #Funciones
          'MAX','MIN','APPEND','CONS', 'FIRST', 'REST', 'APPLY',
          #Tipos de datos
          'NUMERO', 'DECIMAL', 'APLICAR', 'MODULO', 'OPSLAH'

    ]


#EXPRESIONES REGULARES REGLAS PARA SIMPLE
#palabras reservadas
t_MAX = r'MAX'
t_MIN = r'MIN'
t_CONS = r'CONS'
t_APPEND = r'APPEND'
t_FIRST = r'FIRST'
t_REST = r'REST'
t_APPLY = r'APPLY'
t_APLICAR = r'aplicar'


#simbolos
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_QUOTE = r'\'' #apostrofe
#t_SPACE = r'\s'
t_MODULO = r'\%'
t_OPSLAH = r'\//'
t_LCOR = r'\['
t_RCOR = r'\]'


#operadores
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_PLUS = r'\+'


#Tipos de datos de entrada
#t_ALFNUM = r'[\w]+'
#t_STRING = r'[a-zA-Z]'
def t_DECIMAL(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_error(t):
    print("Lexical: illegal character '%s' in line '%d' position" % (t.value[0], t.lineno))
    t.lexer.skip(1)

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t'
lexer = lex.lex()