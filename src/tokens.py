# !/usr/bin/env python
# coding=utf8
# Author: quheng

tokens = [
    'ID',
    'SYS_TYPE',
    'SYS_CON',
    'SYS_PROC',
    'SYS_FUNCT',

    # type
    'INTEGER',
    'REAL',
    'CHAR',
    'BOOLEAN',
    'STRING',

    # symbols
    'LP',
    'PLUS',
    'RP',
    'MINUS',
    'LB',
    'UNEQUAL',
    'RB',
    'GE',
    'DOT',
    'GT',
    'COMMA',
    'SEMI',
    'LE',
    'COLON',
    'LT',
    'MUL',
    'EQUAL',
    'ASSIGN']

t_LP = r"\("
t_RP = r"\)"

t_LB = r"\["
t_RB = r"\]"

t_PLUS = r"\+"
t_MINUS = r"－"
t_MUL = r"\*"


t_GE = r">="
t_GT = r">"
t_LE = r"<="
t_LT = r"<"
t_EQUAL = r"="
t_UNEQUAL = r"<>"

t_DOT = r"\."
t_COMMA = r","
t_SEMI = r";"
t_COLON = r":"

t_ASSIGN = r":="

# reserved words or variable`
reserved = {
    'if': 'IF',
    'program': 'PROGRAM',
    'function': 'FUNCTION',
    'procedure': 'PROCEDURE',
    'array': 'ARRAY',

    'var': 'VAR',
    'record': 'RECORD',
    'of': 'OF',
    'type': 'TYPE',

    'const': 'CONST',

    'begin': 'BEGIN',
    'end': 'END',
    'if': 'IF',
    'else': 'ELSE',
    'then': 'THEN',
    'case': 'CASE',
    'to': 'TO',
    'do': 'DO',
    'downto': 'DOWNTO',
    'goto': 'GOTO',
    'for': 'FOR',
    'while': 'WHILE',
    'repeat': 'REPEAT',
    'until': 'UNTIL',

    'div': 'DIV',
    'mod': 'MOD',
    'not': 'NOT',
    'and': 'AND',
    'or': 'OR', }
#   'xor': 'XOR',
#   'true': 'TRUE',
#   'false': 'FALSE'}

# data type
sys_type = {
    "integer",
    "real",
    "char",
    "string",
    "boolean"
}

sys_proc = {"write", "writeln"}
sys_funct = {"abs", "chr", "odd", "ord", "pred", "sqr", "sqrt", "succ"}

tokens.extend(reserved.values())

def t_ID(t):
    r"[a-zA-Z]([a-zA-Z0-9])*"

    if t.value.lower() in sys_type:
        t.type = "SYS_TYPE"

    if t.value.lower() in sys_proc:
        t.type = "SYS_PROC"

    if t.value.lower() in sys_funct:
        t.type = "SYS_FUNCT"

    if t.value.lower() in reserved:
        t.type = reserved[t.value.lower()]
    return t

t_REAL = r"(\-)*[0-9]+\.[0-9]+"
t_INTEGER = r"(\-)*[0-9]+"

def t_CHAR(t):
    r"(\'([^\\\'])\')|(\"([^\\\"])\")"
    return t

def t_STRING(t):
    r"(\"([^\\\"]|(\\.))*\")|(\'([^\\\']|(\\.))*\')"
    escaped = 0
    str = t.value[1:-1]
    new_str = ""
    for i in range(0, len(str)):
        c = str[i]
        if escaped:
            if c == "n":
                c = "\n"
            elif c == "t":
                c = "\t"
            new_str += c
            escaped = 0
        else:
            if c == "\\":
                escaped = 1
            else:
                new_str += c
    t.value = new_str
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
            s = raw_input('pas: ')
        except EOFError:
            break
        if not s:
            continue
        lexer.input(s)
        for tok in lexer:
            print(tok)
