import ply.yacc as yacc
import lexer  # Import lexer information

tokens = lexer.tokens  #


def p_error(p):
    print("Lexical: illegal character '%s' in line '%d' position" % (p.value[0], p.lineno))
    p.yacc.skip(1)


def p_atomo(p):
    '''atomo : STRING
             | NUM
             | ALFNUM
    '''
#Funcion FIRST: devuelve el primer elemento de una lista
def p_first(p):
    '''first : LPAREN APPLY SPACE QUOTE FIRST SPACE QUOTE lista RPAREN
    '''

#Funcion REST: devuelve el ultimo elemento de una lista
def p_rest(p):
    '''rest : LPAREN APPLY SPACE QUOTE REST SPACE QUOTE lista RPAREN
    '''

#Funcion CONS: ingresa un atomo a una lista
def p_cons(p):
    '''cons : LPAREN APPLY SPACE QUOTE CONS SPACE QUOTE lista RPAREN
    '''

#Funcion PLUS : Suma los elementos de una lista
def p_plus(p):
    '''first : LPAREN APPLY SPACE QUOTE PLUS SPACE QUOTE lista RPAREN
    '''

#Funcion TIMES : Multiplica los elementos de una lista
def p_times(p):
    '''first : LPAREN APPLY SPACE QUOTE TIMES SPACE QUOTE lista RPAREN
    '''

#Funcion DIVIDE : Divide los elementos de una lista
def p_divide(p):
    '''first : LPAREN APPLY SPACE QUOTE DIVIDE SPACE QUOTE lista RPAREN
    '''

#Funcion RESTA : Divide los elementos de una lista
def p_minus(p):
    '''first : LPAREN APPLY SPACE QUOTE MINUS SPACE QUOTE lista RPAREN
    '''


#Funcion MAX: Devuelve el valor máximo de una lista
def p_max(p):
    '''max : LPAREN APPLY SPACE QUOTE MAX SPACE QUOTE lista RPAREN
    '''

#Funcion MIN: Devuelve el valor minimo de una lista
def p_min(p):
    '''min : LPAREN APPLY QUOTE MIN SPACE QUOTE lista RPAREN
    '''
    
def p_lista(p):
    '''lista : LPAREN RPAREN 
             | LPAREN atomo RPAREN
             | LPAREN atomo SPACE atomo SPACE lista RPAREN
             | LPAREN atomo SPACE atomo SPACE lista SPACE atomo RPAREN '''
