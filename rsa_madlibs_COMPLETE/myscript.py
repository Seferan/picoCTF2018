#!/usr/bin/env python

import re
import pwn
from Crypto.Util.number import inverse

#nc 2018shell.picoctf.com 50652

host, port = '2018shell.picoctf.com', 50652

s= pwn.remote(host,port)

print '='*5 + 'PROBLEM 1' + '='*5

prompt = s.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
s.sendline('y')
print prompt
q = int(re.findall('q : (.*)', prompt)[0])
p = int(re.findall('p : (.*)', prompt)[0])
next_prompt = prompt.split('\n')[-2] + ':'
prompt = s.recvuntil(next_prompt)
print prompt
n = p * q
s.sendline(str(n))
#s.sendline('8815769761')

print '='*5 + 'PROBLEM 2' + '='*5

prompt = s.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print prompt
p = int(re.findall('p : (.*)', prompt)[0])
n = int(re.findall('n : (.*)', prompt)[0])
s.sendline('y')
next_prompt = prompt.split('\n')[-2] + ':'
prompt = s.recvuntil(next_prompt)
print prompt
q = n / p
s.sendline(str(q))
#s.sendline('77773')

print '='*5 + 'PROBLEM 3' + '='*5

prompt = s.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print prompt
s.sendline('n')

print '='*5 + 'PROBLEM 4' + '='*5

prompt = s.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print prompt
p = int(re.findall('p : (.*)', prompt)[0])
q = int(re.findall('q : (.*)', prompt)[0])
s.sendline('y')
next_prompt = prompt.split('\n')[-2] + ':'
prompt = s.recvuntil(next_prompt)
print prompt
#formula totient(n) = (p-1)*(q-1)
#AKA phi
totient_n = (p-1)*(q-1)
s.sendline(str(totient_n))
#s.sendline('6256003596')

print '='*5 + 'PROBLEM 5' + '='*5

prompt = s.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print prompt

plaintext = int(re.findall('plaintext : (.*)', prompt)[0])
e = int(re.findall('e : (.*)', prompt)[0])
n = int(re.findall('n : (.*)', prompt)[0])
s.sendline('y')
next_prompt = prompt.split('\n')[-2] + ':'
prompt = s.recvuntil(next_prompt)
print prompt

ciphertext = pow(plaintext, e, n)
s.sendline(str(ciphertext))
#s.sendline('26722917505435451150596710555980625220524134812001687080485341361511207096550823814926607028717403343344600191255790864873639087129323153797404989216681535785492257030896045464472300400447688001563694767148451912130180323038978568872458130612657140514751874493071944456290959151981399532582347021031424096175747508579453024891862161356081561032045394147561900547733602483979861042957169820579569242714893461713308057915755735700329990893197650028440038700231719057433874201113850357283873424698585951160069976869223244147124759020366717935504226979456299659682165757462057188430539271285705680101066120475874786208053')

print '='*5 + 'PROBLEM 6' + '='*5

prompt = s.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print prompt
s.sendline('n')

print '='*5 + 'PROBLEM 7' + '='*5

prompt = s.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print prompt
q = int(re.findall('q : (.*)', prompt)[0])
p = int(re.findall('p : (.*)', prompt)[0])
e = int(re.findall('e : (.*)', prompt)[0])
s.sendline('y')
next_prompt = prompt.split('\n')[-2] + ':'
prompt = s.recvuntil(next_prompt)
print prompt
n=p*q
phi = (p-1)*(q-1)
d = inverse(e, phi)
s.sendline(str(d))
#s.sendline('1405046269503207469140791548403639533127416416214210694972085079171787580463776820425965898174272870486015739516125786182821637006600742140682552321645503743280670839819078749092730110549881891271317396450158021688253989767145578723458252769465545504142139663476747479225923933192421405464414574786272963741656223941750084051228611576708609346787101088759062724389874160693008783334605903142528824559223515203978707969795087506678894006628296743079886244349469131831225757926844843554897638786146036869572653204735650843186722732736888918789379054050122205253165705085538743651258400390580971043144644984654914856729')

print '='*5 + 'PROBLEM 8' + '='*5
prompt = s.recvuntil('IS THIS POSSIBLE and FEASIBLE? (Y/N):')
print prompt
p = int(re.findall('p : (.*)', prompt)[0])
ciphertext = int(re.findall('ciphertext : (.*)', prompt)[0])
e = int(re.findall('e : (.*)', prompt)[0])
n = int(re.findall('n : (.*)', prompt)[0])
s.sendline('y')
next_prompt = prompt.split('\n')[-2] + ':'
prompt = s.recvuntil(next_prompt)
print prompt
q = n / p
phi = (p-1)*(q-1)
d = inverse(e, phi)
plaintext = pow(ciphertext, d, n)
s.sendline(str(plaintext))
#s.sendline('240109877286251840533272915662757983981706320845661471802585807564915966910385147086109038271870589')

print '='*5 + 'END OF TASK' + '='*5

ending = s.recvuntil("If you convert the last plaintext to a hex number, then ascii, you'll find what you're searching for ;)")
print ending
s.close()

print hex(plaintext)[2:].decode('hex')
#print (hex(240109877286251840533272915662757983981706320845661471802585807564915966910385147086109038271870589)[2:]).decode('hex')




