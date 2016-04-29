# !/usr/bin/env python
# coding=utf8
# Author: quheng

tokens = (
    'NAME',
    'NUMBER',)

t_ignore = " \t"
literals = ['=', '+', '-', '*', '/', '(', ')']

t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

import ply.lex as lex
lex.lex()
