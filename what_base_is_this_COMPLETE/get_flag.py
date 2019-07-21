#!/usr/bin/env python

import pwn
import re

host, port = '2018shell.picoctf.com', 1225

s = pwn.remote(host, port)

prompt = s.recv()

#print prompt

binary = re.findall('the (.*) as a word', prompt)[0]
#'01100110 01101100 01111001 01100101 01110010'
# remove the spaces
# convert to int base 2
# view as hex
# [2:] index 2 until the end...Removes the 0x at start of 0x12341234
# finally decode to hex (ascii)....not sure why its not decode('ascii')
answer =  hex(int(binary.replace(' ',''),2))[2:].decode('hex')

#print "Sending answer: " + answer
s.sendline(answer)

prompt = s.recv()

#print prompt

hexword = re.findall('the (.*) as a word', prompt)[0]

answer = hexword.decode('hex')

s.sendline(answer)

prompt = s.recv()

oct = re.findall('the (.*) as a word', prompt)[0]

#print oct.split(' ')[1:]
# good way to operate on everything
# print [x for x in oct.split(' ')[1:]]

# interpret as base 8
# print [int(x,8) for x in oct.split(' ')[1:]]

# convert to characters
#print [chr(int(x,8)) for x in oct.split(' ')[1:]]

#join it all together
#print ''.join([chr(int(x,8)) for x in oct.split(' ')[1:]])

answer = ''.join([chr(int(x,8)) for x in oct.split(' ')[1:]])

s.sendline(answer)

prompt = s.recv()

print re.findall('picoCTF{.*}', prompt)[0]




#print hex(int(oct.replace(' ',''),10))[2:].decode('hex')
#print hex(int(dec.replace(' ','')))[
#binary = re.findall('the (.*) as a word', prompt)[0]

#print answer




#first = '01100110 01101100 01111001 01100101 01110010'

#first_split = first.split(" ")

#first_split_with_bs = map(lambda x: '0b'+x,first_split)
