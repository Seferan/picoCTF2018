#! /usr/bin/env python

import sys

msg = 'd]Wc7H:oW5YgUFS7]D\9fGS^iGHSUF9bHSg9WIf9q'

# we guess that the last character is a }
# also the first couple chracters should be picoCTF{
# between q and } is 12 characters
# so we lastly need to figure out the "wrap around" value.  
# our first guess was correct

wrap_around_char = '}'

msgint = map(ord,list(msg))

for i in range(1,256):
	msgint = map(lambda x: x+1, msgint)
	msgint = map(lambda x: x-26 if x > ord(wrap_around_char) else x, msgint)
	result = map(chr,msgint)
	result_string = "".join(result)
	# check to see if our output contains picoCTF and stop.
	if 'picoCTF' in result_string:
		break;

print str(i) + ": " +  result_string
	



