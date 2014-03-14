#!/usr/bin/python
#test.py

import re
import sys

sampleText = open(sys.argv[1], "r")
sampleRead = sampleText.read()

#regex = re.compile('YEAR') 

for line in sampleRead.splitlines():
    if "YEAR" in line:
        print line