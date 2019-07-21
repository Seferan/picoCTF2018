#!/bin/bash

# reverse, then cut based on spaces, grabbing first field then reverse again
# Username: Password: picoCTF{J0hn_1$_R1pp3d_289677b5}
# grabs just the last part
(echo 'root'; echo 'password1') | nc 2018shell.picoctf.com 5221 | rev | cut -d " " -f1 | rev


