#!/usr/bin/env python

from pwn import *

context.log_level = 'critical'

def solve_unit(problem, answer):
	split_problem = problem.split(' + ')
	result = solve(split_problem)
	if result == answer:
		print 'SUCCESS! ' + result + ' == ' + answer
		return 0
	else:
		print 'FAIL! ' + result + ' == ' + answer
		return -1

def calc_depth(val):
	max_depth = 0
	depth = 0
	for char in val:
		if depth > max_depth:
			max_depth = depth
		if char == '(':
			depth +=1
		elif char == ')':
		 	depth -=1
		else:
			print 'ERROR!!!!'
	#print val + ': ' + str(max_depth)
	return max_depth


def solve_two(problem):
	prob1 = problem[0]
	prob2 = problem[1]
	depth1 = calc_depth(prob1)
	depth2 = calc_depth(prob2)
	if depth1 < depth2:
		#print '<'
		result = '(' + prob1 + prob2[1:]
	elif depth1 > depth2:
		#print '>'
		result = prob1[:-1] + prob2 + ')'
	else:
		#print '=='
		result = prob1 + prob2
	return result

def solve(problem):
	if len(problem) > 2:
		# if greater than 2, than merge first two, then recurse on next.
		first = solve_two(problem[:2])
		return solve([first]+problem[2:])
	else:
		return "".join(solve_two(problem[:2]))


unit_test1 = '() + () = ()()'                                   #   => [combine]
unit_test2 = '((())) + () = ((())())'                           #   => [absorb-right]
unit_test3 = '() + ((())) = (()(()))'                           #   => [absorb-left]
unit_test4 = '(())(()) + () = (())(()())'                       #   => [combined-absorb-right]
unit_test5 = '() + (())(()) = (()())(())'                       #   => [combined-absorb-left]
unit_test6 = '(())(()) + ((())) = ((())(())(()))'                 # => [absorb-combined-right]
unit_test7 = '((())) + (())(()) = ((())(())(()))'                 # => [absorb-combined-left]
#() + (()) + ((())) = (()()) + ((())) = ((()())(()))' # => [left-associative]
unit_test8 = '() + (()) + ((())) = ((()())(()))' # => [left-associative]


unit_tests = [unit_test1,unit_test2,unit_test3,unit_test4,unit_test5,unit_test6,unit_test7,unit_test8]
unit_tests = map(lambda x:x.split(' = '), unit_tests)

# solve unit tests
print 'Performing Unit Tests'
print '='*25
map(lambda x:solve_unit(x[0],x[1]),unit_tests)
print '='*25

host, port = '2018shell.picoctf.com', 22973

s = remote(host,port)

while True:
	prompt = s.recvline()
	if '???' in prompt:
		problem = prompt.split(' = ')[0].split(' + ')
		print problem
		result = solve(problem)
		s.recvuntil('>')
		print 'Prompt: ' + prompt
		print 'Answer: ' + result
		s.sendline(result)
	elif 'flag' in prompt:
		print prompt
		break

