#!/usr/bin/env python

import numpy

fib = {}
fib[1] = 1
fib[2] = 1
for i in range(1084):
	if i == 0:
		print 'Start of Fib'
	elif i == 1 or i == 2:
		print str(i) + ': ' + str(fib[i])
	else:
		fib[i] = numpy.int32(fib[i-1]+fib[i-2])
		print str(i) + ': ' + str(fib[i])


