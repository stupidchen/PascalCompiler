# !/usr/bin/env python
# coding=utf8
# Author: quheng

import llvmlite.ir as ir
import llvmlite.binding as llvm
import sys
from ctypes import CFUNCTYPE, c_double, c_int, c_void_p, cast, c_int32

import non_terminal as nt
import Node

class SymbleTable(object):
    def __init__(self):
        # 变量
        self.var_table = {}

        # table
        self.fn_table = {}

        # question
        self.scope_var = {}
        self.scope_fn = {}

        # type
        self.type_table = {}
        self.scope_type = {}

    def add_var(self, var_name, addr, scope_id, var_type=None):
        """
        将变量加入符号表
        """
        self.var_table.setdefault(var_name, []).append((addr, var_type))
        self.scope_var.setdefault(scope_id, []).append(var_name)

    def add_fn(self, fn_name, fn_block, scope_id):
        """
        将函数加入符号表
        """
        self.fn_table.setdefault(fn_name, []).append(fn_block)
        self.scope_fn.setdefault(scope_id, []).append(fn_name)

    # question
    def add_type(self, name, type_def, scope_id):
        self.type_table.setdefault(name, []).append(type_def)
        self.scope_type.setdefault(scope_id, []).append(name)

    def fetch_var_addr(self, var_name):
        """
        获取变量
        """
        o = self.var_table.get(var_name, None)
        if o:
            return o[-1][0]
        else:
            raise CodegenError('Can not find symble {0}'.format(var_name))

    # question
    def fetch_var_addr_type(self, var_name):
        o = self.var_table.get(var_name, None)
        if o:
            return o[-1]
        else:
            raise CodegenError('Can not find symble {0}'.format(var_name))

    def fetch_fn_block(self, fn_name):
        """
        获取函数
        """
        o = self.fn_table.get(fn_name, None)
        if o:
            return o[-1]
        else:
            raise CodegenError('Can not find function {0}'.format(fn_name))

    def fetch_type(self, type_name):
        o = self.type_table.get(type_name, None)
        if o:
            return o[-1]
        else:
            raise CodegenError('Can not find type {0}'.format(type_name))

    # def remove_var(self, var_name):
    #     o = self.var_table.get(var_name, None)
    #     if o:
    #         del o[-1]
    #     else:
    #         raise CodegenError('Remove var {0} that not exsists!'.format(var_name))

    # question
    def remove_scope(self, scope_id):
        for name in self.scope_var.get(scope_id, []):
            o = self.var_table.get(name, None)
            if o:
                del o[-1]
            else:
                raise CodeGenerator('Remove var {0} that not exsists!'.format(name))
        del self.scope_var[scope_id]
        scope_id += 1
        for name in self.scope_fn.get(scope_id, []):
            o = self.fn_table.get(name, None)
            if o:
                del o[-1]
            else:
                raise CodeGenerator('Remove var {0} that not exsists!'.format(name))
        if scope_id in self.scope_fn:
            del self.scope_fn[scope_id]

def do_write(x):
    print x

def do_read(x):
    x = int(raw_input())
    return x

do_write_type = ir.FunctionType(ir.VoidType(), (ir.IntType(32),))
c_do_write_type = CFUNCTYPE(c_void_p, c_int32)
c_do_write = c_do_write_type(do_write)
do_write_addr = cast(c_do_write, c_void_p).value

do_read_type = ir.FunctionType(ir.IntType(32), (ir.IntType(32), ))
c_do_read_type = CFUNCTYPE(c_int32, c_int32)
c_do_read = c_do_read_type(do_read)
do_read_addr = cast(c_do_read, c_void_p).value


class Generator(object):
    """docstring for """
    def __init__(self):
        super(Generator, self).__init__()

        # 初始化符号表
        self.sym_table = SymbleTable()

        # 当前 IR builder.
        self.builder = None

    def generate(self, node):
        if node.__class__ is Node.Node:
            if node.type == nt.program:
                self.generate(node.args[0])
                self.generate(node.args[1])
            elif node.type == nt.program_head:
                self.module = ir.Module(node.args[0])
            elif node.type == nt.routine:
                pass
            elif node.type == nt.sub_routine:
                pass
            elif node.type == nt.routine_head:
                pass
            elif node.type == nt.const_part:
                pass
            elif node.type == nt.const_expr_list:
                pass
            elif node.type == nt.const_value:
                pass
            elif node.type == nt.type_part:
                pass
            elif node.type == nt.type_decl_list:
                pass
            elif node.type == nt.type_definition:
                pass
            elif node.type == nt.type_decl:
                pass
            elif node.type == nt.array_type_decl:
                pass
            elif node.type == nt.field_decl_list:
                pass
            elif node.type == nt.field_decl:
                pass
            elif node.type == nt.name_list:
                pass
            elif node.type == nt.simple_type_decl:
                pass
            elif node.type == nt.var_part:
                pass
            elif node.type == nt.var_decl_list:
                pass
            elif node.type == nt.var_decl:
                pass
            elif node.type == nt.routine_part:
                pass
            elif node.type == nt.function_decl:
                pass
            elif node.type == nt.function_head:
                pass
            elif node.type == nt.procedure_decl:
                pass
            elif node.type == nt.procedure_head:
                pass
            elif node.type == nt.parameters:
                pass
            elif node.type == nt.para_decl_list:
                pass
            elif node.type == nt.para_type_list:
                pass
            elif node.type == nt.var_para_list:
                pass
            elif node.type == nt.routine_body:
                pass
            elif node.type == nt.stmt_list:
                pass
            elif node.type == nt.stmt:
                pass
            elif node.type == nt.non_label_stmt:
                pass
            elif node.type == nt.assign_stmt:
                pass
            elif node.type == nt.proc_stmt:
                pass
            elif node.type == nt.compound_stmt:
                pass
            elif node.type == nt.if_stmt:
                pass
            elif node.type == nt.else_clause:
                pass
            elif node.type == nt.repeat_stmt:
                pass
            elif node.type == nt.while_stmt:
                pass
            elif node.type == nt.for_stmt:
                pass
            elif node.type == nt.direction:
                pass
            elif node.type == nt.case_stmt:
                pass
            elif node.type == nt.case_expr_list:
                pass
            elif node.type == nt.case_expr:
                pass
            elif node.type == nt.goto_stmt:
                pass
            elif node.type == nt.expression_list:
                pass
            elif node.type == nt.expression:
                pass
            elif node.type == nt.expr:
                pass
            elif node.type == nt.term:
                pass
            elif node.type == nt.factor:
                pass
            elif node.type == nt.args_list:
                pass
            elif node.type == nt.record_type_decl:
                pass

    def _type_helper(self, type):


def generate(ast):
    generator = Generator()
    print generator
    print "1"
    generator.generate(ast)
    return generator.module
