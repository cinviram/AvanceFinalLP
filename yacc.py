import ply.yacc as yacc

from lex import tokens

name = {}

def cons(1)
    return [1[0]] + 1[1]
name['cons'] = cons

def concat(1):
    return 1[0] + 1[1]
name['concat'] = concat()

def listar(1):
    return 1
name['list'] = listar

