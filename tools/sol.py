#!/usr/bin/env python

from __future__ import print_function
import sys
import os

if len(sys.argv) != 2:
    print("Usage: sol.py filename")
    sys.exit(-1)

filename = sys.argv[1]

with open(filename, 'r') as f:
    print(f.read())


os.system('python ' + filename)
