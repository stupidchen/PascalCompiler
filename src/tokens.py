# !/usr/bin/env python
# coding=utf8
# Author: quheng

tokens = [
    'IDENTIFIER',
    'NUMBER']

# reserved words or variable
reserved = {
    'if': 'IF'
}
tokens.extend(reserved.values())
def t_IDENTIFIER(t):
    r"[a-zA-Z]([a-zA-Z0-9])*"
    if t.value.lower() in reserved:
        t.type = reserved[t.value.lower()]
    return t


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


if __name__ == "__main__":
    import ply.lex as lex
    lexer = lex.lex()
    while 1:
        try:
            s = raw_input('calc > ')
        except EOFError:
            break
        if not s:
            continue
        lexer.input(s)
        for tok in lexer:
            print(tok)
