#!/bin/bash

#downloaded exiftool for this challenge
#displays file metadata
exiftool 2018.png | grep -oE "picoCTF{.*}"

