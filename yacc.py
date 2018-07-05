import ply.yacc as yacc
from lexer import tokens  # Import lexer information
resultado_gramatica = []
 #



'''

def p_error(p):
    print("Lexical: illegal character '%s' in line '%d' position" % (p.value[0], p.lineno))
    p.yacc.skip(1)
'''

def p_atomo(p):
    '''atomo : STRING
             | NUM
             | ALFNUM
    '''
    pass

def p_lista(p):
    '''lista : LPAREN RPAREN 
             | LPAREN atomo RPAREN
             | LPAREN atomo SPACE atomo RPAREN
             | LPAREN atomo SPACE atomo SPACE lista RPAREN
             | LPAREN atomo SPACE atomo SPACE lista SPACE atomo RPAREN '''
    pass

#Funcion FIRST: devuelve el primer elemento de una lista
def p_first(p):
    '''first : LPAREN APPLY SPACE FIRST lista RPAREN
    '''
    pass

#Funcion REST: devuelve el ultimo elemento de una lista
def p_rest(p):
    '''rest : LPAREN APPLY SPACE REST lista RPAREN
    '''
    pass

#Funcion CONS: ingresa un atomo a una lista
def p_cons(p):
    '''cons : LPAREN APPLY SPACE CONS lista RPAREN
    '''
    pass

#Funcion PLUS : Suma los elementos de una lista
def p_plus(p):
    '''plus : LPAREN APPLY SPACE PLUS lista RPAREN
    '''
    pass

#Funcion TIMES : Multiplica los elementos de una lista
def p_times(p):
    '''times : LPAREN APPLY SPACE TIMES lista RPAREN'''
    pass

#Funcion DIVIDE : Divide los elementos de una lista
def p_divide(p):
    '''divide : LPAREN APPLY SPACE DIVIDE lista RPAREN'''
    pass

#Funcion RESTA : Resta los elementos de una lista
def p_minus(p):
    'minus : LPAREN APPLY SPACE MINUS lista RPAREN'
    pass


#Funcion MAX: Devuelve el valor maximo de una lista
def p_max(p):
    '''max : LPAREN APPLY SPACE MAX lista RPAREN'''
    pass

#Funcion MIN: Devuelve el valor minimo de una lista
def p_min(p):
    '''min : LPAREN APPLY SPACE MIN lista RPAREN'''
    pass

#Funcion APPEND: Concatena dos listas
def p_append(p):
    '''append : LPAREN APPLY SPACE APPEND LPAREN lista SPACE lista RPAREN RPAREN'''
    pass

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {} en el valor {}".format( str(t.type),str(t.value))
        print(resultado)
    else:
        resultado = "Error sintactico {}".format(t)
        print(resultado)
    resultado_gramatica.append(resultado)


# instanciamos el analizador sistactico
parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
    resultado_gramatica.clear()

    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else: print("data vacia")

    print("result: ", resultado_gramatica)
    return resultado_gramatica

if __name__ == '__main__':
    while True:
        try:
            s = input(' ingresa dato >>> ')
        except EOFError:
            continue
        if not s: continue

        # gram = parser.parse(s)
        # print("Resultado ", gram)

        prueba_sintactica(s)