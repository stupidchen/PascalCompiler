# !/usr/bin/env python
# coding=utf8
# Author: quheng
from Node import Node
import non_terminal as nt

precedence = (
    ('left', 'GE', 'GT', 'LE', 'LT', 'EQUAL'),
    ('left', 'PLUS', 'MINUS', 'OR'),
    ('left', 'MUL', 'DIV', 'MOD', 'AND'),
    ('right', 'NOT'),
)

def p_program(t):
    'program : program_head routine DOT'
    t[0] = Node(nt.program, t[1], t[2])

def p_program_head(t):
    'program_head : PROGRAM  ID  SEMI'
    t[0] = Node(nt.program_head, t[2])

def p_routine(t):
    'routine : routine_head  routine_body'
    t[0] = Node(nt.routine, t[1], t[2])

def p_sub_routine(t):
    'sub_routine : routine_head  routine_body'
    # 'sub_routine : routine_body'
    t[0] = Node(nt.sub_routine, t[1], t[2])

def p_routine_head(t):
    'routine_head : label_part  const_part  type_part  var_part routine_part'
    t[0] = Node(nt.routine_head, t[1], t[2], t[3], t[4], t[5])

def p_label_part(t):
    'label_part : epsilon'
    t[0] = Node(nt.label_part)

def p_const_part(t):
    """
    const_part : CONST  const_expr_list
                | epsilon
    """
    if (len(t) == 2):
        t[0] = Node(nt.const_part)
    else:
        t[0] = Node(nt.const_part, t[2])

def p_const_expr_list(t):
    """
    const_expr_list : const_expr_list  ID  EQUAL  const_value  SEMI
            |  ID  EQUAL  const_value  SEMI
    """
    if (len[t] == 6):
        t[0] = Node(nt.const_expr_list, t[1], t[2], t[3])
    else:
        t[0] = Node(nt.const_expr_list, t[1], t[2])

def p_const_value(t):
    """
    const_value : INTEGER
                |  REAL
                |  CHAR
                |  STRING
                |  SYS_CON
    """
    t[0] = Node(nt.const_value, t[1])

def p_type_part(t):
    """
    type_part : TYPE type_decl_list
            |  epsilon
    """
    if (len(t) == 3):
        t[0] = Node(nt.type_part, t[2])
    else:
        t[0] = Node(nt.type_part)

def p_type_decl_list(t):
    """
    type_decl_list : type_decl_list  type_definition
                  |  type_definition
    """
    if (len(t) == 3):
        t[0] = Node(nt.type_decl_list, t[1], t[2])
    else:
        t[0] = Node(nt.type_decl_list, t[1])

def p_type_definition(t):
    """
    type_definition : ID  EQUAL  type_decl  SEMI
    """
    t[0] = Node(nt.p_type_definition, t[1], t[3])

def p_type_decl(t):
    """
    type_decl : simple_type_decl
            | array_type_decl
            | record_type_decl
    """
    t[0] = Node(nt.type_decl, t[1])

def p_array_type_decl(t):
    """
    array_type_decl : ARRAY  LB  simple_type_decl  RB  OF  type_decl
    """
    t[0] = Node(nt.array_type_decl, t[3], t[6])

def p_field_decl_list(t):
    """
    field_decl_list : field_decl_list  field_decl
                    |  field_decl
    """
    if (len(t) == 3):
        t[0] = Node(nt.field_decl_list, t[1], t[2])
    else:
        t[0] = Node(nt.field_decl_list, t[1])

def p_field_decl(t):
    """
    field_decl : name_list  COLON  type_decl  SEMI
    """
    t[0] = Node(nt.field_decl, t[1], t[3])

def p_name_list(t):
    """
    name_list : name_list  COMMA  ID
            |  ID
    """
    if (len(t) == 4):
        t[0] = Node(nt.name_list, t[1], t[3])
    else:
        t[0] = Node(nt.name_list, t[1])

def p_simple_type_decl(t):
    """
    simple_type_decl : SYS_TYPE
                |  ID
                |  LP  name_list  RP
                |  const_value  DOT DOT  const_value
                |  ID  DOT DOT  ID
                |  MINUS  const_value  DOT DOT  const_value
                |  MINUS  const_value  DOT DOT  MINUS const_value
    """
    if (len(t) == 2):
        t[0] = Node(nt.simple_type_decl, t[1])
    elif(len(t) == 4):
        t[0] = Node(nt.simple_type_decl, t[2])
    elif(len(t) == 5):
        if (t[1].type == nt.const_value):
            t[0] = Node(nt.simple_type_decl, t[1], t[4])
        else:
            t[0] = Node(nt.simple_type_decl, t[1], t[4])
    elif(len(t) == 6):
        t[0] = Node(nt.simple_type_decl, t[2], t[5])
    elif(len(t) == 7):
        t[0] = Node(nt.simple_type_decl, t[2], t[6])

def p_var_part(t):
    """
    var_part : VAR  var_decl_list
            |  epsilon
    """
    if (len(t) == 3):
        t[0] = Node(nt.var_part, t[2])
    else:
        t[0] = Node(nt.var_part)

def p_var_decl_list(t):
    """
    var_decl_list :  var_decl_list  var_decl
                |  var_decl
    """
    if (len(t) == 3):
        t[0] = Node(nt.var_decl_list, t[1], t[2])
    else:
        t[0] = Node(nt.var_decl_list, t[1])

def p_var_decl(t):
    """
    var_decl :  name_list  COLON  type_decl  SEMI
    """
    t[0] = Node(nt.var_decl, t[1], t[3])

def p_routine_part(t):
    """
    routine_part : routine_part  function_decl
           |  routine_part  procedure_decl
           |  function_decl
           |  procedure_decl
           |  epsilon
    """
    if (len(t) == 3):
        t[0] = Node(nt.routine_part, t[1], t[2])
    else:
        t[0] = Node(nt.var_decl, t[1])

def p_function_decl(t):
    """
    function_decl : function_head  SEMI  sub_routine  SEMI
    """
    t[0] = Node(nt.function_decl, t[1], t[3])

def p_function_head(t):
    """
    function_head :  FUNCTION  ID  parameters  COLON  simple_type_decl
    """
    t[0] = Node(nt.function_head, t[2], t[3], t[5])

def p_procedure_decl(t):
    """
    procedure_decl :  procedure_head  SEMI  sub_routine  SEMI
    """
    t[0] = Node(nt.procedure_decl, t[1], t[3])

def p_procedure_head(t):
    """
    procedure_head :  PROCEDURE ID parameters
    """
    t[0] = Node(nt.procedure_head, t[2], t[3])

def p_parameters(t):
    """
    parameters : LP  para_decl_list  RP
            |  epsilon
    """
    if (len(t) == 4):
        t[0] = Node(nt.parameters, t[2])
    else:
        t[0] = Node(nt.parameters)

def p_para_decl_list(t):
    """
    para_decl_list : para_decl_list  SEMI  para_type_list
                        | para_type_list
    """
    if (len(t) == 4):
        t[0] = Node(nt.para_decl_list, t[1], t[3])
    else:
        t[0] = Node(nt.para_decl_list)

def p_para_type_list(t):
    """
    para_type_list : var_para_list COLON  simple_type_decl
    """
    t[0] = Node(nt.para_type_list, t[1], t[3])

def p_var_para_list(t):
    """
    var_para_list : VAR  name_list
                | name_list
    """
    if (len(t) == 3):
        t[0] = Node(nt.var_para_list, t[2])
    else:
        t[0] = Node(nt.var_para_list, t[1])

def p_routine_body(t):
    """
    routine_body : compound_stmt
    """
    t[0] = Node(nt.routine_body, t[1])

def p_stmt_list(t):
    """
    stmt_list : stmt_list  stmt  SEMI
            |  epsilon
    """
    if (len(t) == 4):
        t[0] = Node(nt.stmt_list, t[1], t[2])
    else:
        t[0] = Node(nt.stmt_list)

def p_stmt(t):
    """
    stmt : INTEGER  COLON  non_label_stmt
        |  non_label_stmt
    """
    if (len(t) == 4):
        t[0] = Node(nt.stmt, t[3])
    else:
        t[0] = Node(nt.stmt, t[1])

def p_non_label_stmt(t):
    """
    non_label_stmt : assign_stmt
                | proc_stmt
                | compound_stmt
                | if_stmt
                | repeat_stmt
                | while_stmt
                | for_stmt
                | case_stmt
                | goto_stmt
    """
    t[0] = Node(nt.non_label_stmt, t[1])

def p_assign_stmt(t):
    """
    assign_stmt : ID  ASSIGN  expression
           | ID LB expression RB ASSIGN expression
           | ID  DOT  ID  ASSIGN  expression
    """
    if (len(t) == 4):
        t[0] = Node(nt.assign_stmt, t[1], t[3])
    elif(len(t) == 7):
        t[0] = Node(nt.assign_stmt, t[3], t[6])
    elif(len(t) == 6):
        t[0] = Node(nt.assign_stmt, t[1], t[2], t[5])

def p_proc_stmt(t):    # question
    """
    proc_stmt : ID
          |  SYS_PROC
          |  ID  LP  args_list  RP
          |  SYS_PROC  LP  expression_list  RP
    """
    #           |  READ  LP  factor  RP
    if (len(t) == 2):
        t[0] = Node(nt.proc_stmt, t[1])
    elif(len(t) == 5):
        t[0] = Node(nt.proc_stmt, t[1], t[3])
    elif(len(t) == 2):
        t[0] = Node(nt.proc_stmt, t[1], t[3])

def p_compound_stmt(t):
    """
    compound_stmt : BEGIN  stmt_list  END
    """
    t[0] = Node(nt.compound_stmt, t[2])

def p_if_stmt(t):
    """
    if_stmt : IF  expression  THEN  stmt  else_clause
    """
    # IF  expression  THEN  start  else_clause
    t[0] = Node(nt.if_stmt, t[2], t[4], t[5])

def p_else_clause(t):
    """
    else_clause : ELSE stmt
                |  epsilon
    """
    if (len(t) == 3):
        t[0] = Node(nt.else_clause, t[2])
    else:
        t[0] = Node(nt.else_clause)

def p_repeat_stmt(t):
    """
    repeat_stmt : REPEAT  stmt_list  UNTIL  expression
    """
    t[0] = Node(nt.repeat_stmt, t[2], t[4])

def p_while_stmt(t):
    """
    while_stmt : WHILE  expression  DO stmt
    """
    t[0] = Node(nt.while_stmt, t[2], t[4])

def p_for_stmt(t):
    """
    for_stmt : FOR  ID  ASSIGN  expression  direction  expression  DO stmt
    """
    t[0] = Node(nt.for_stmt, t[2], t[4], t[5], t[6], [8])

def p_direction(t):
    """
    direction : TO
              | DOWNTO
    """
    t[0] = Node(nt.direction, t[1])

def p_case_stmt(t):
    """
    case_stmt : CASE expression OF case_expr_list  END
    """
    t[0] = Node(nt.case_stmt, t[2], t[4])

def p_case_expr_list(t):
    """
    case_expr_list : case_expr_list  case_expr
                   |  case_expr
    """
    if (len(t) == 2):
        t[0] = Node(nt.case_expr_list, t[1], t[2])
    else:
        t[0] = Node(nt.case_expr_list, t[1])

def p_case_expr(t):
    """
    case_expr : const_value  COLON  stmt  SEMI
          |  ID  COLON  stmt  SEMI
    """
    t[0] = Node(nt.case_expr, t[1], t[3])

def p_goto_stmt(t):
    """
    goto_stmt : GOTO  INTEGER
    """
    t[0] = Node(nt.goto_stmt, t[2])

def p_expression_list(t):
    """
    expression_list : expression_list  COMMA  expression
                    | expression
    """
    if (len(t) == 4):
        t[0] = Node(nt.expression_list, t[1], t[3])
    else:
        t[0] = Node(nt.expression_list, t[1])

def p_expression(t):
    """
    expression : expression  GE  expr
          |  expression  GT  expr
          |  expression  LE  expr
          |  expression  LT  expr
          |  expression  EQUAL  expr
          |  expression  UNEQUAL  expr
          |  expr
    """
    if (len(t) == 2):
        t[0] = Node(nt.expression, t[1])
    else:
        t[0] = Node(nt.expression, t[1], t[2], t[3])

def p_expr(t):
    """
    expr : expr  PLUS  term
        |  expr  MINUS  term
        |  expr  OR  term
        |  term

    """
    if (len(t) == 4):
        t[0] = Node(nt.expr, t[1], t[2], t[3])
    else:
        t[0] = Node(nt.expr, t[1])

def p_term(t):
    """
    term : term  MUL  factor
        |  term  DIV  factor
        |  term  MOD  factor
        |  term  AND  factor
        |  factor
    """
    if (len(t) == 4):
        t[0] = Node(nt.term, t[1], t[2], t[3])
    else:
        t[0] = Node(nt.term, t[1])

def p_factor(t):
    """
    factor : ID
        |  const_value
        |  NOT  factor
        |  MINUS  factor
        |  ID  DOT  ID
        |  LP  expression  RP
        |  ID  LB  expression  RB
        |  ID  LP  args_list  RP
        |  SYS_FUNCT SYS_FUNCT  LP  args_list  RP
    """
    if (len(t) == 2):
        t[0] = Node(nt.factor, t[1])
    elif (len(t) == 3):
        t[0] = Node(nt.factor, t[1], t[2])
    elif (len(t) == 4):
        t[0] = Node(nt.factor, t[1], t[2], t[3])
    elif (len(t) == 5):
        t[0] = Node(nt.factor, t[1], t[2], t[3], t[4])
    elif (len(t) == 6):
        t[0] = Node(nt.factor, t[1], t[2], t[3], t[4], t[5])

def p_args_list(t):
    """
    args_list : args_list  COMMA  expression
            |  expression
    """
    if (len(t) == 4):
        t[0] = Node(nt.args_list, t[1], t[3])
    else:
        t[0] = Node(nt.args_list, t[1])

def p_record_type_decl(t):
    """
    record_type_decl : RECORD  field_decl_list  END
    """
    t[0] = Node(nt.record_type_decl, t[2])

def p_epsilon(p):
    'epsilon :'
    pass

def p_error(p):
    if p:
        print("Syntax error at '%s', line %d" % (p.value, p.lineno))
    else:
        print("Syntax error at EOF")
