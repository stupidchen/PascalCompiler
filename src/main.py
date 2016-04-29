# !/usr/bin/env python
# coding=utf8
# Author: quheng

from tokens import tokens

def t_NUMBER(t):
    r'\d+'     # 描述模式的正则表达式
    t.value = int(t.value)
    return t     # 最后必须返回t，如果不返回，这个token就会被丢弃掉
