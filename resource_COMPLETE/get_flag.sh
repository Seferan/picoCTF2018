#!/bin/bash

# -o return only
# -E regular expression format
# .* means all characters
# -s on curl means silent

curl -s "https://picoctf.com/resources" | grep -oE "picoCTF{.*}"

