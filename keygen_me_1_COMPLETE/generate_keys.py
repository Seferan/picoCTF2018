#!/usr/bin/env python

# import for string constants: https://docs.python.org/2/library/string.html#string-constants
import string
import pwn
#have to import like this to get context variable
from pwn import *
import re
import random

#importing to allow me to write to output without a new line.
import sys

context.log_level= 'critical'

valid_chars = string.digits + string.ascii_uppercase

key_attempt = list('0'*16)
print 'Starting search for valid keys...'
while True:
	new_char = random.choice(valid_chars)
	index = random.choice(range(16))
	key_attempt[index] = new_char
	key_str =  "".join(key_attempt)
	elf = pwn.ELF('./activate')
	arglist = []
	arglist.append(key_str)
	p = elf.process(arglist)
	output = p.recv()
	if output.startswith('INVALID'):
		sys.stdout.write('.')
	else:
		print '' # new line
		print key_str + ': '+ output.replace('\n','')
