#!/usr/bin/env python

import base64 
orig_cookie = 'lmsTXXkEcx0D6u2z0EUQjdz0whpOBPGXuJClyiVzfYMZaBSKmZoZcrD9YWcyiYwKdhGcqXTK2sKYQ4PCRQ/Fw/HQwNTZ6UksJI/OKmfkL7E='
ciphertext = base64.b64decode(orig_cookie)

# take first 10 bytes, then grab 11th and XOR that with 0x1 to flip one bit, then append remaining cipher text.
result=ciphertext[0:10]+chr(ord(ciphertext[10])^0x1)+ciphertext[11:]
print orig_cookie
print base64.b64encode(result)

