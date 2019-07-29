#!/usr/bin/env python

n = {}

for i in range(102220):
	if i <= 0x4:
		n[i] = i*i+0x2345
	else:
		n[i] = n[i-5]*0x1234 + n[i-1] - n[i-2] + n[i-3] - n[i-4]
		n[i] = n[i] & 0xFFFFFFFF
	print str(i) + ': ' + str(n[i]) + ': ' + hex(n[i])

#print n
