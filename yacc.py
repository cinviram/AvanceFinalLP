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
    '''first : LPAREN APPLY QUOTE FIRST SPACE QUOTE lista RPAREN 
    '''

#Funcion REST: devuelve el ultimo elemento de una lista
def p_rest(p):
    '''rest : LPAREN APPLY QUOTE REST SPACE QUOTE lista RPAREN 
    '''

#Funcion CONS: ingresa un atomo a una lista
def p_cons(p):
    '''cons : LPAREN APPLY QUOTE CONS SPACE QUOTE lista RPAREN 
    '''


def p_lista(p):
    '''lista : LPAREN RPAREN 
             | LPAREN atomo RPAREN
             | LPAREN atomo SPACE atomo SPACE lista RPAREN
             | LPAREN atomo SPACE atomo SPACE lista SPACE atomo RPAREN '''
