	.section	__TEXT,__text,regular,pure_instructions
	.macosx_version_min 15, 5
	.globl	_writeln
	.align	4, 0x90
_writeln:
	.cfi_startproc
	movabsq	$4359221088, %rax
	jmpq	*%rax
	.cfi_endproc

	.globl	_readln
	.align	4, 0x90
_readln:
	.cfi_startproc
	movabsq	$4359221040, %rax
	jmpq	*%rax
	.cfi_endproc

	.globl	_main
	.align	4, 0x90
_main:
	.cfi_startproc
	pushq	%rbp
Ltmp0:
	.cfi_def_cfa_offset 16
	pushq	%r15
Ltmp1:
	.cfi_def_cfa_offset 24
	pushq	%r14
Ltmp2:
	.cfi_def_cfa_offset 32
	pushq	%r13
Ltmp3:
	.cfi_def_cfa_offset 40
	pushq	%r12
Ltmp4:
	.cfi_def_cfa_offset 48
	pushq	%rbx
Ltmp5:
	.cfi_def_cfa_offset 56
	pushq	%rax
Ltmp6:
	.cfi_def_cfa_offset 64
Ltmp7:
	.cfi_offset %rbx, -56
Ltmp8:
	.cfi_offset %r12, -48
Ltmp9:
	.cfi_offset %r13, -40
Ltmp10:
	.cfi_offset %r14, -32
Ltmp11:
	.cfi_offset %r15, -24
Ltmp12:
	.cfi_offset %rbp, -16
	movabsq	$_fib, %rbx
	movl	$1, %edi
	callq	*%rbx
	movl	%eax, 4(%rsp)
	movl	$2, %edi
	callq	*%rbx
	movl	%eax, (%rsp)
	movl	$3, %edi
	callq	*%rbx
	movl	%eax, %r12d
	movl	$4, %edi
	callq	*%rbx
	movl	%eax, %r13d
	movl	$5, %edi
	callq	*%rbx
	movl	%eax, %r15d
	movl	$6, %edi
	callq	*%rbx
	movl	%eax, %ebp
	movl	$7, %edi
	callq	*%rbx
	movl	%eax, %r14d
	movabsq	$_writeln, %rbx
	movl	4(%rsp), %edi
	callq	*%rbx
	movl	(%rsp), %edi
	callq	*%rbx
	movl	%r12d, %edi
	callq	*%rbx
	movl	%r13d, %edi
	callq	*%rbx
	movl	%r15d, %edi
	callq	*%rbx
	movl	%ebp, %edi
	callq	*%rbx
	movl	%r14d, %edi
	movq	%rbx, %rax
	addq	$8, %rsp
	popq	%rbx
	popq	%r12
	popq	%r13
	popq	%r14
	popq	%r15
	popq	%rbp
	jmpq	*%rax
	.cfi_endproc

	.globl	_fib
	.align	4, 0x90
_fib:
	pushq	%rbp
	pushq	%r14
	pushq	%rbx
	movl	%edi, %ebx
	movl	$1, %ebp
	cmpl	$2, %ebx
	jb	LBB3_3
	movabsq	$_fib, %r14
	.align	4, 0x90
LBB3_2:
	leal	-2(%rbx), %edi
	callq	*%r14
	decl	%ebx
	addl	%eax, %ebp
	cmpl	$1, %ebx
	ja	LBB3_2
LBB3_3:
	movl	%ebp, %eax
	popq	%rbx
	popq	%r14
	popq	%rbp
	retq


.subsections_via_symbols
