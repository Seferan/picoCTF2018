#!/usr/bin/env python

#import numpy
from numpy import subtract

msg = 'llkjmlmpadkkc'.upper()
key = 'thisisalilkey'.upper()

# convert both into lists 
# ['T', 'H', 'I', 'S', 'I', 'S', 'A', 'L', 'I', 'L', 'K', 'E', 'Y']
list(msg)
list(key)

# map will run function (ord) on each object in list
# ord converstion ascii to int
msgint = map(ord,list(msg))
keyint = map(ord,list(key))

# Subtract off value of "A" from each to do the vignere cipher
keyintshift = map(lambda x: x-ord('A'), keyint)

# substract key from msg
resultints = subtract(msgint, keyintshift)

#resultints2 = map(lambda x: x-26 if x>ord('Z') else x, resultints)

# any values that are less than ord('A') are no longer letters and need to wrap around.
resultints3 = map(lambda x: x+26 if x<ord('A') else x, resultints)

result = map(chr,resultints3)

print "picoCTF{" + "".join(result) + "}"
