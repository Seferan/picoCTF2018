#!/bin/bash

# using bash to call python is a bit strange, but w/e
python -c "print 'picoCTF{%s}' % 'dGg0dF93NHNfczFtcEwz'.decode('base64')"
