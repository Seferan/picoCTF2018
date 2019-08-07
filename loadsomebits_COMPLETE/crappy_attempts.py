#!/usr/bin/env python

import binascii
import struct

image = open('pico2018-special-logo.bmp', 'rb').read()

header_field = image[0:2]
size = image[2:6]
size_int = struct.unpack('i', size)[0]
starting_address = image[10:14]
#print binascii.hexlify(starting_address)

header_size = image[14:18]
#print binascii.hexlify(header_size)

without_headers = image[54:100]

my_byte = ''
s = ''
#for c in without_headers:
#	s += chr(ord('0')+(c & 1))
#	print type(c)
#	print c & 1

image = image[54:]
q = 0
answer=''
s=''
for c in image:
	print str(str(ord(c) & 0x01)
	#s+= chr(ord('0')+(int(c) & 1))
	if (len(s)==8):
		if s=='00000000':
			break
		else:
			print 'not zeros'
	
