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
    pass

#Funcion FIRST: devuelve el primer elemento de una lista
def p_first(p):
    '''first : LPAREN APPLY SPACE QUOTE FIRST SPACE QUOTE lista RPAREN
    '''
    pass

#Funcion REST: devuelve el ultimo elemento de una lista
def p_rest(p):
    '''rest : LPAREN APPLY SPACE QUOTE REST SPACE QUOTE lista RPAREN
    '''
    pass

#Funcion CONS: ingresa un atomo a una lista
def p_cons(p):
    '''cons : LPAREN APPLY SPACE QUOTE CONS SPACE QUOTE lista RPAREN
    '''
    pass 

#Funcion PLUS : Suma los elementos de una lista
def p_plus(p):
    '''plus : LPAREN APPLY SPACE QUOTE PLUS SPACE QUOTE lista RPAREN
    '''
    pass

#Funcion TIMES : Multiplica los elementos de una lista
def p_times(p):
    '''times : LPAREN APPLY SPACE QUOTE TIMES SPACE QUOTE lista RPAREN
    '''
    pass

#Funcion DIVIDE : Divide los elementos de una lista
def p_divide(p):
    '''divide : LPAREN APPLY SPACE QUOTE DIVIDE SPACE QUOTE lista RPAREN
    '''
    pass

#Funcion RESTA : Resta los elementos de una lista
def p_minus(p):
    '''minus : LPAREN APPLY SPACE QUOTE MINUS SPACE QUOTE lista RPAREN
    '''
    pass


#Funcion MAX: Devuelve el valor máximo de una lista
def p_max(p):
    '''max : LPAREN APPLY SPACE QUOTE MAX SPACE QUOTE lista RPAREN
    '''
    pass

#Funcion MIN: Devuelve el valor minimo de una lista
def p_min(p):
    '''min : LPAREN APPLY QUOTE MIN SPACE QUOTE lista RPAREN
    '''
    pass

#Funcion APPEND: Concatena dos listas
def p_append(p):
    '''append : LPAREN APPLY SPACE QUOTE APPEND SPACE QUOTE LPAREN lista SPACE lista RPAREN RPAREN
    '''
    pass
    
def p_lista(p):
    '''lista : LPAREN RPAREN 
             | LPAREN atomo RPAREN
             | LPAREN atomo SPACE atomo RPAREN
             | LPAREN atomo SPACE atomo SPACE lista RPAREN
             | LPAREN atomo SPACE atomo SPACE lista SPACE atomo RPAREN '''
    pass


parser = yacc.yacc()
print("Ingrese Exit para terminar")
while True:
    try:
        s = input("Ingrese: ")
        if s == 'Exit':
            break
    except EOFError:
            break

    if not s: continue
        resultado = parser.parse(s)
