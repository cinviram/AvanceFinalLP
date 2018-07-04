
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

<<<<<<< HEAD
_lr_signature = 'QUOTE STRING NUM ALFNUM LPAREN RPAREN PLUS MINUS DIVIDE TIMES MAX MIN APPEND CONS FIRST REST SPACE APPLY TRUEatomo : STRING\n             | NUM\n             | ALFNUM\n    first : LPAREN APPLY SPACE QUOTE FIRST SPACE QUOTE lista RPAREN\n    rest : LPAREN APPLY SPACE QUOTE REST SPACE QUOTE lista RPAREN\n    cons : LPAREN APPLY SPACE QUOTE CONS SPACE QUOTE lista RPAREN\n    plus : LPAREN APPLY SPACE QUOTE PLUS SPACE QUOTE lista RPAREN\n    times : LPAREN APPLY SPACE QUOTE TIMES SPACE QUOTE lista RPAREN\n    divide : LPAREN APPLY SPACE QUOTE DIVIDE SPACE QUOTE lista RPAREN\n    minus : LPAREN APPLY SPACE QUOTE MINUS SPACE QUOTE lista RPAREN\n    max : LPAREN APPLY SPACE QUOTE MAX SPACE QUOTE lista RPAREN\n    min : LPAREN APPLY QUOTE MIN SPACE QUOTE lista RPAREN\n    append : LPAREN APPLY SPACE QUOTE APPEND SPACE QUOTE LPAREN lista SPACE lista RPAREN RPAREN\n    lista : LPAREN RPAREN \n             | LPAREN atomo RPAREN\n             | LPAREN atomo SPACE atomo RPAREN\n             | LPAREN atomo SPACE atomo SPACE lista RPAREN\n             | LPAREN atomo SPACE atomo SPACE lista SPACE atomo RPAREN '
=======
_lr_signature = 'QUOTE STRING NUM ALFNUM LPAREN RPAREN PLUS MINUS DIVIDE TIMES MAX MIN APPEND CONS FIRST REST SPACE APPLY TRUEatomo : STRING\n             | NUM\n             | ALFNUM\n    first : LPAREN APPLY SPACE QUOTE FIRST SPACE QUOTE LPAREN SPACE atomo SPACE atomo SPACE RPAREN RPAREN\n    rest : LPAREN APPLY SPACE QUOTE REST SPACE QUOTE lista RPAREN\n    cons : LPAREN APPLY SPACE QUOTE CONS SPACE QUOTE lista RPAREN\n    plus : LPAREN APPLY SPACE QUOTE PLUS SPACE QUOTE lista RPAREN\n    times : LPAREN APPLY SPACE QUOTE TIMES SPACE QUOTE lista RPAREN\n    divide : LPAREN APPLY SPACE QUOTE DIVIDE SPACE QUOTE lista RPAREN\n    minus : LPAREN APPLY SPACE QUOTE MINUS SPACE QUOTE lista RPAREN\n    max : LPAREN APPLY SPACE QUOTE MAX SPACE QUOTE lista RPAREN\n    min : LPAREN APPLY QUOTE MIN SPACE QUOTE lista RPAREN\n    append : LPAREN APPLY SPACE QUOTE APPEND SPACE QUOTE LPAREN lista SPACE lista RPAREN RPAREN\n    lista : LPAREN RPAREN \n             | LPAREN atomo RPAREN\n             | LPAREN atomo SPACE atomo RPAREN\n             | LPAREN atomo SPACE atomo SPACE atomo RPAREN\n             | LPAREN atomo SPACE atomo SPACE lista RPAREN\n             | LPAREN atomo SPACE atomo SPACE lista SPACE atomo RPAREN '
>>>>>>> 2363ffe600cc3a208e819d2d86de4bd88de3f6ff
    
_lr_action_items = {'STRING':([0,],[2,]),'NUM':([0,],[3,]),'ALFNUM':([0,],[4,]),'$end':([1,2,3,4,],[0,-1,-2,-3,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'atomo':([0,],[1,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> atomo","S'",1,None,None,None),
  ('atomo -> STRING','atomo',1,'p_atomo','yacc.py',13),
  ('atomo -> NUM','atomo',1,'p_atomo','yacc.py',14),
  ('atomo -> ALFNUM','atomo',1,'p_atomo','yacc.py',15),
  ('first -> LPAREN APPLY SPACE QUOTE FIRST SPACE QUOTE LPAREN SPACE atomo SPACE atomo SPACE RPAREN RPAREN','first',15,'p_first','yacc.py',21),
  ('rest -> LPAREN APPLY SPACE QUOTE REST SPACE QUOTE lista RPAREN','rest',9,'p_rest','yacc.py',27),
  ('cons -> LPAREN APPLY SPACE QUOTE CONS SPACE QUOTE lista RPAREN','cons',9,'p_cons','yacc.py',33),
  ('plus -> LPAREN APPLY SPACE QUOTE PLUS SPACE QUOTE lista RPAREN','plus',9,'p_plus','yacc.py',39),
  ('times -> LPAREN APPLY SPACE QUOTE TIMES SPACE QUOTE lista RPAREN','times',9,'p_times','yacc.py',45),
  ('divide -> LPAREN APPLY SPACE QUOTE DIVIDE SPACE QUOTE lista RPAREN','divide',9,'p_divide','yacc.py',51),
  ('minus -> LPAREN APPLY SPACE QUOTE MINUS SPACE QUOTE lista RPAREN','minus',9,'p_minus','yacc.py',57),
  ('max -> LPAREN APPLY SPACE QUOTE MAX SPACE QUOTE lista RPAREN','max',9,'p_max','yacc.py',64),
  ('min -> LPAREN APPLY QUOTE MIN SPACE QUOTE lista RPAREN','min',8,'p_min','yacc.py',70),
  ('append -> LPAREN APPLY SPACE QUOTE APPEND SPACE QUOTE LPAREN lista SPACE lista RPAREN RPAREN','append',13,'p_append','yacc.py',76),
  ('lista -> LPAREN RPAREN','lista',2,'p_lista','yacc.py',81),
  ('lista -> LPAREN atomo RPAREN','lista',3,'p_lista','yacc.py',82),
  ('lista -> LPAREN atomo SPACE atomo RPAREN','lista',5,'p_lista','yacc.py',83),
<<<<<<< HEAD
  ('lista -> LPAREN atomo SPACE atomo SPACE lista RPAREN','lista',7,'p_lista','yacc.py',84),
  ('lista -> LPAREN atomo SPACE atomo SPACE lista SPACE atomo RPAREN','lista',9,'p_lista','yacc.py',85),
=======
  ('lista -> LPAREN atomo SPACE atomo SPACE atomo RPAREN','lista',7,'p_lista','yacc.py',84),
  ('lista -> LPAREN atomo SPACE atomo SPACE lista RPAREN','lista',7,'p_lista','yacc.py',85),
  ('lista -> LPAREN atomo SPACE atomo SPACE lista SPACE atomo RPAREN','lista',9,'p_lista','yacc.py',86),
>>>>>>> 2363ffe600cc3a208e819d2d86de4bd88de3f6ff
]
