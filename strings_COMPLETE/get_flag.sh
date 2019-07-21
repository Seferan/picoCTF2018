#!/bin/bash

# E means allow regular expresses
strings strings | grep -oE "picoCTF{.*}"

