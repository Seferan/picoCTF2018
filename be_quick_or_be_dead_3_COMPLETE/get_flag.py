#!/usr/bin/env python

from pwn import *
import os
#http://docs.pwntools.com/en/stable/elf/elf.html#module-members
#can insert assembly, and then save with ELF.save()

context.log_level = 'critical'

elf = ELF('./be-quick-or-be-dead-3')

#for key, address in elf.symbols.iteritems():
#	print key, hex(address)

# want to remove alarm call

number = 0x2f8cdc3f

elf.asm( elf.symbols['alarm'], 'ret' )

#replace the "calc" function with simply returning the value we found..
elf.asm( elf.symbols['calc'], 'mov eax,%s\nret\n' % (hex(number & 0xFFFFFFFF)))
#save the new binary
elf.save('./new_calc')
os.system('chmod +x ./new')
p = process('./new')
p.poll(True)
