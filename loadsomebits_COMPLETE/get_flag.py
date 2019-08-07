#!/usr/bin/env python

import binascii
import struct

HEADER_SIZE = 54

image = open('pico2018-special-logo.bmp', 'rb')
header = image.read(HEADER_SIZE)

message = ''

while True:
	new_byte = ''
	for bit in range(8):
		# read one byte at a time
		next_byte = image.read(1)
		# ord = given character, return integer which allows us to do bitwise &
		new_byte += str(ord(next_byte) & 0x01)

	n = int(new_byte,2)
	if n == 0:
		break
	message += binascii.unhexlify('%x' % n)


print message
