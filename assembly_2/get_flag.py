#!/usr/bin/env python

#asm2(0x8,0x21)
ebp_plus_0x8 = 0x8
ebp_plus_0xc = 0x21

eax = ebp_plus_0xc
ebp_minus_0x4 = eax
eax = ebp_plus_0x8
ebp_minus_0x8 = eax

# skip to part_b

while ebp_plus_0x8 < 0x3923:
    ebp_minus_0x4 += 1
    ebp_plus_0x8 += 0xa9

eax = ebp_minus_0x4

print hex(eax)
