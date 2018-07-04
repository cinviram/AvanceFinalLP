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




def p_apply(p):
    '''


    '''

def p_lista(p):
    '''lista : LPAREN RPAREN 
             | LPAREN atomo RPAREN
             | LPAREN atomo SPACE atomo SPACE lista RPAREN
             | LPAREN atomo SPACE atomo SPACE lista SPACE atomo RPAREN '''
