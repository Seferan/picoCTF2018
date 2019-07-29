#!/usr/bin/env python

from pwn import unhex

#c: 6248240025043854684405555049971462176821736811257920561518478991864242765793684
#n: 12251761860944483606751883449696528080072010141745857839539893207146089191955171
#e: 65537


#https://stackoverflow.com/a/9758173/5387119
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

c= 6248240025043854684405555049971462176821736811257920561518478991864242765793684
n= 12251761860944483606751883449696528080072010141745857839539893207146089191955171
e= 65537

#https://www.alpertron.com.ar/ECM.HTM
#this gave us Euler's Totient:
phi = int('12 251761 860944 483606 751883 449696 528079 969386 689071 166982 693118 468674 586166 505552'.replace(' ', ''))
#phi = (p-1)*(q-1)

d=modinv(e,phi)
m=pow(c,d,n)

print(unhex(hex(m)[2:]))



#https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
