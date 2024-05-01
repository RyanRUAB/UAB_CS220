	.file	"asgn5.c"							#This is the current file being compiled
	.text										#This is the start of the code that is being converted to assembly
	.globl	myAddTwoNumbersFunction				#Allows myAddTwoNumbersFunction to be seen by other files
	.type	myAddTwoNumbersFunction, @function	#Information about what type myAddTwoNumbersFunction is (in this case a function)
myAddTwoNumbersFunction:						#The start of the myAddTwoNumbersFunction
.LFB0:											#This is a label, a memory location of an instruction, similar to a pointer
	.cfi_startproc								#.cfi
	pushq	%rbp								#Pushes the register %rbp to the top of the stack, the start of the preamble
	.cfi_def_cfa_offset 16						#.cfi
	.cfi_offset 6, -16							#.cfi
	movq	%rsp, %rbp							#Sets the register %rbp to the stack pointer %rsp making it the frame pointer, end of the preamble
	.cfi_def_cfa_register 6						#.cfi
	movl	%edi, -4(%rbp)						#Sets a local variable on the stack frame (one here)
	movl	%esi, -8(%rbp)						#Sets a local variable on the stack frame (two here)
	movl	-4(%rbp), %edx						#Sets a local variable to a register (one here)
	movl	-8(%rbp), %eax						#Sets a local variable to a register (two here)
	addl	%edx, %eax							#Adds %edx and %eax, then sets %eax to the result
	popq	%rbp								#Removes %rbp from the stack, removes the stack frame
	.cfi_def_cfa 7, 8							#.cfi
	ret											#the return value of the function (one + two / %eax)
	.cfi_endproc								#.cfi
.LFE0:											#This is a label, a memory location of an instruction, similar to a pointer
	.size	myAddTwoNumbersFunction, .-myAddTwoNumbersFunction	#Denotes the size of the function between the labels
	.section	.rodata							#Applies a section name to this part of the code, this is used by the linker
.LC0:											#This is a label, a memory location of an instruction, similar to a pointer
	.string	"The answer is %d\n"				#Initializes the string to be used in the printf function
	.text										#The start of the code being converted to assembly, specifically the start of the main function
	.globl	main								#Allows main to be seen by other files
	.type	main, @function						#Information about what type main is (in this case a function)
main:											#Start of the main function
.LFB1:											#This is a label, a memory location of an instruction, similar to a pointer
	.cfi_startproc								#.cfi
	pushq	%rbp								#Pushes the register %rbp to the top of the stack, the start of the preamble
	.cfi_def_cfa_offset 16						#.cfi
	.cfi_offset 6, -16							#.cfi
	movq	%rsp, %rbp							#Sets the register %rbp to the stack pointer %rsp, end of the preamble
	.cfi_def_cfa_register 6						#.cfi
	subq	$16, %rsp							#Makes space for local variables
	movl	$10, -12(%rbp)						#Sets local variable on the stack (x)
	movl	$7, -8(%rbp)						#Sets local variable on the stack (y)
	movl	$0, -4(%rbp)						#Sets local variable on the stack (answer)
	movl	-8(%rbp), %edx						#Sets local variable (y) to the register %edx
	movl	-12(%rbp), %eax						#Sets local variable (x) to the register %eax
	movl	%edx, %esi							#Sets register %edx to %esi, this will be used in myAddTwoNumbersFunction
	movl	%eax, %edi							#Sets register %eax to %edi, this will be used in myAddTwoNumbersFunction
	call	myAddTwoNumbersFunction				#Calls the myAddTwoNumbersFunction to be used in main
	movl	%eax, -4(%rbp)						#Sets the %eax register onto the stack
	movl	-4(%rbp), %eax						#Sets the local variable back to %eax register 
	movl	%eax, %esi							#Sets the %eax register to the %esi register, this is the answer of myAddTwoNumbersFunction
	leaq	.LC0(%rip), %rdi					#Sets the address of the label .LC0 to %rdi, this is setting the string from .LC0 to %rdi
	movl	$0, %eax							#Sets the %eax register, the return register, to zero
	call	printf@PLT							#calls the printf function to print the previous string and answer
	movl	$0, %eax							#Sets the %eax register, the return register, to zero
	leave										#Removes the stack frame for the main function
	.cfi_def_cfa 7, 8							#.cfi
	ret											#The return value of the main function (in this case a 0)
	.cfi_endproc								#.cfi
.LFE1:											#This is a label, a memory location of an instruction, similar to a pointer
	.size	main, .-main						#Denotes the size of the function between the labels
	.ident	"GCC: (Ubuntu 7.5.0-3ubuntu1~18.04) 7.5.0"	#Creates a comment which seems to denote which version of GCC
	.section	.note.GNU-stack,"",@progbits	#Applies a section name to this part of the code, this is used by the linker
