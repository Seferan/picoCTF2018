#!/usr/bin/env python

#import pwn
from pwn import *
import re

context.log_level= 'critical'

elf = ELF('./main')

lookup = {}

for i in range(33, 127):
	my_char = chr(i)
	p = elf.process()

	p.sendline(my_char)
	prompt = p.recvall()

	result = re.findall('ciphertext: (.*)', prompt)[0]
	lookup[result] = my_char
	# print my_char + ': ' + result

	ct = re.findall('Now quack it! : (.*)', prompt)[0]


#print lookup
pt =  map(lambda x: lookup[x], ct.split())
flag = "".join(pt)

print flag
