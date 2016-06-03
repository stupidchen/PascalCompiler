# !/usr/bin/env python
# coding=utf8
# Author: quheng

from __init__ import *

import ply.lex as lex
import ply.yacc as yacc
import argparse

import draw_graphic
import codegenerate


parser = argparse.ArgumentParser()
parser.add_argument('-d', '--draw', action='store_true', help='draw the syntax abstract tree')
args = parser.parse_args()

lexer = lex.lex()
yacc.yacc()

if __name__ == "__main__":
    f = open("/Users/quheng/Documents/Workspace/python/learn/PascalCompiler/test/test.p")
    ast = yacc.parse(f.read(), debug = False)
    # parser.parse_args(['-d'])
    if args.draw:
        draw_graphic.graph(ast, 'test')

    codegenerate.generate(ast)
    # print ast
    # data = '''3 + 4 * 10+ -20 *2'''
    # lexer.input(data)
    # for tok in lexer:
    #     print(tok)
