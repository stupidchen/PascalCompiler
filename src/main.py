# !/usr/bin/env python
# coding=utf8
# Author: quheng

from __init__ import *

import ply.lex as lex
import ply.yacc as yacc

lex.lex()
yacc.yacc()

if __name__ == "__main__":
    while 1:
        try:
            s = raw_input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        yacc.parse(s)
