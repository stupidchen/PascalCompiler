import llvmlite.ir as ir
import llvmlite.binding as llvm
from backend.codegen import CodeGenerator,PascalParser
import argparse
import sys
from ctypes import CFUNCTYPE,c_double,c_int,c_void_p,cast,c_int32


arg_parser=argparse.ArgumentParser()
arg_parser.add_argument("input_file",help='specify the input file')
arg_parser.add_argument("-O","--optimization_level",action='store_true',help="specify the optimization level")
arg_parser.add_argument("-i","--ir_file",help="generate ir code")
arg_parser.add_argument("-a","--assembly_file",help="generate assembly file")
args=arg_parser.parse_args()

parser=PascalParser()
codestr=open(args.input_file,'r').read()
ast=parser.parse(codestr)
if not ast:
    sys.exit(0)

llvm.initialize()
llvm.initialize_native_target()
llvm.initialize_native_asmprinter()

target=llvm.Target.from_default_triple()
codegen=CodeGenerator('main')
codegen.generate_code(ast)
ir_code=str(codegen.module)
llvmmod=llvm.parse_assembly(str(codegen.module))

if args.optimization_level:
    pmb=llvm.create_pass_manager_builder()
    pmb.opt_level=3
    pm=llvm.create_module_pass_manager()
    pmb.populate(pm)
    pm.run(llvmmod)
    ir_code=str(llvmmod)

if args.ir_file:
    with open(args.ir_file,'w') as f:
        f.write(ir_code)

target_machine=target.create_target_machine()

with llvm.create_mcjit_compiler(llvmmod,target_machine) as ee:
    ee.finalize_object()
    if args.assembly_file:
        with open(args.assembly_file,'w') as f:
            f.write(target_machine.emit_assembly(llvmmod))
    func=llvmmod.get_function('main')
    fptr=CFUNCTYPE(c_void_p)(ee.get_pointer_to_function(func))
    result=fptr()
