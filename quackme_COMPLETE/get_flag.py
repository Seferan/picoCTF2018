#!/usr/bin/env python

#pip install pwntools

import re
import pwn

greeting_message = "You have now entered the Duck Web, and you're in for a honkin' good time.\nCan you figure out my trick?"

# got xor string from sekret buffer.  Copied into visual studio code and massaged
xor_string = '\x29\x06\x16\x4f\x2b\x35\x30\x1e\x51\x1b\x5b\x14\x4b\x08\x5d\x2b\x56\x47\x57\x50\x16\x4d\x51\x51\x5d\x00'

print re.findall('picoCTF{.*?}', pwn.xor(greeting_message, xor_string))[0]
