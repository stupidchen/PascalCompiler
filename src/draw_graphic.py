# !/usr/bin/env python
# coding=utf8
# Author: quheng

import pydot
from Node import Node

def graph(node, filename):
    edges = descend(node)
    g = pydot.graph_from_edges(edges)
    if filename:
        f = filename + ".png"
    else:
        f = "graph.png"
    g.write_png(f, prog='dot')


def descend(node):
    edges = []
    if node.__class__ != Node:
        return edges
    for i in node.args:
        edges.append((s(node), s(i)))
        edges += descend(i)
    return edges


def s(node):
    if node.__class__ is Node:
        return "%s (%s)" % (node.type, id(node))
    else:
        return "%s (%s)" % (node, id(node))
