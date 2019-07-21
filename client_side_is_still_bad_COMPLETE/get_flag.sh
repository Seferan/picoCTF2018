#!/bin/bash

#    checkpass = document.getElementById("pass").value;
#    split = 4;
#    if (checkpass.substring(split*7, split*8) == '}') {
#      if (checkpass.substring(split*6, split*7) == 'd366') {
#        if (checkpass.substring(split*5, split*6) == 'd_3b') {
#         if (checkpass.substring(split*4, split*5) == 's_ba') {
#          if (checkpass.substring(split*3, split*4) == 'nt_i') {
#            if (checkpass.substring(split*2, split*3) == 'clie') {
#              if (checkpass.substring(split, split*2) == 'CTF{') {
#                if (checkpass.substring(0,split) == 'pico') {
#                  alert("You got the flag!")

# first filter out to only checkpass.substring
# then regular expression to get only the parts between ' '
# use tac to reverse the order
# use awk to put all the entries on a single line
# sed to replace ' with blank
curl -s "http://2018shell.picoctf.com:55790/index.html" | grep "checkpass.substring" | grep -oE "'.*'" | tac | awk '{print}' ORS='' | sed "s/'//g"

