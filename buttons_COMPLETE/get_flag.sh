#!/bin/bash

curl -s -X 'POST' http://2018shell.picoctf.com:44730/button2.php | grep -oE "picoCTF{.*}"
