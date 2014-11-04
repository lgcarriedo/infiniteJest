#!/usr/bin/env python
#parser3.py
#Ciera Martinez
#There are two arguments 1. file that 

import re
import sys	
from collections import Counter

#This sets up output file
orig_stdout = sys.stdout

sampleText = open(sys.argv[1]) #file that contains text
listOfTerms = open(sys.argv[2]) #file that contains terms to search for

sampleRead = sampleText.read() #Makes a one item string
termRead = listOfTerms.read() 

termSplit = termRead.split('\r') #splits term list by carriage return

sampleReadCh = sampleRead.split('<ch>')

print sampleReadCh

sampleClean = re.sub('[^A-Za-z0-9\s]+', '', sampleRead) #removes symbols

#print sampleClean
wordData = {}
for word in termSplit:
    wordData[word] = sampleClean.count(word) 

#print wordData

sampleText.close()
listOfTerms.close()
