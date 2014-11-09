#!/usr/bin/env python
#chp3.py
#Ciera Martinez

#There are two arguments 
#1. a file that containts text to search
#2. a file that contains terms to search for 


import re
import sys	
from collections import Counter

#This sets up output file
orig_stdout = sys.stdout

sampleText = open(sys.argv[1]) #file that contains text ex. 
listOfTerms = open(sys.argv[2]) #file that contains terms to search for

sampleRead = sampleText.read() #Makes a one item string
termRead = listOfTerms.read() 

termSplit = termRead.split('\r') #splits term list by carriage return

sampleReadCh = sampleRead.split('<ch>')

sampleClean = re.sub('[^A-Za-z0-9\s]+', '', sampleRead) #removes symbols

#print sampleClean
wordData = {}
for word in termSplit:
    wordData[word] = sampleClean.count(word) 

#print wordData

sampleText.close()
listOfTerms.close()
