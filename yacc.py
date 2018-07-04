import ply.yacc as yacc
import lexer  # Import lexer information

tokens = lexer.tokens  #


def p_error(p):
    print("Lexical: illegal character '%s' in line '%d' position" % (p.value[0], p.lineno))
    p.yacc.skip(1)


def p_apply(p):
    '''


    '''


def p_lista(p):
    '''lista : LPAREN RPAREN 
             | LPAREN ATOMO RPAREN
             | LPAREN ATOMO SPACE ATOMO RPAREN
             | LPAREN ATOMO SPACE ATOMO RPAREN
             | LPAREN ATOMO SPACE LPAREN ATOMO SPACE ATOMO RPAREN ATOMO RPAREN '''