#!/usr/bin/env python
#parser.py
#Ciera Martinez

import re
import sys	
from collections import Counter

#This sets up output file
orig_stdout = sys.stdout

sampleText = open(sys.argv[1]) #file that contains text
#listOfTerms = open(sys.argv[2]) #file that contains terms to search for

sampleRead = sampleText.read() #Makes a one item string
#termRead = listOfTerms.read() 

#Need to split by new line
# termSplit = termRead.split()

sampleReadClean = re.sub('[^A-Za-z0-9\s]+', '', sampleRead) #removes symbols

#counter
word_set = ['Hal', 'Tony', 'Orin']
freq = {}
for word in word_set:
    freq[word] = sampleReadClean.count(word) 

print freq

sampleText.close()
#listOfTerms.close()

