#! /usr/bin/env python

import sys

#dumps out all 26 rotations of the key. 
#look thru manually to find correct one.

msg = 'picoCTF{grpqxdllaliazxbpxozfmebotlvlicmr}'
msg = 'grpqxdllaliazxbpxozfmebotlvlicmr'
msgint = map(ord,list(msg))


for i in range(1,27):
	msgint = map(lambda x: x+1, msgint)
	msgint = map(lambda x: x-26 if x > ord('z') else x, msgint)
	result = map(chr,msgint)
	print str(i) + "-picoCTF{" + "".join(result) + "}"



