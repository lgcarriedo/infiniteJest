#!/usr/bin/env python
#parser.py
#Ciera Martinez

import re
import sys	

sampleText = open(sys.argv[1]) #file that contains text
listOfTerms = open(sys.argv[2]) #file that contains terms to search for
 
sampleRead = sampleText.read() #Makes a one item string
termRead = listOfTerms.read() 

sampleReadClean = re.sub('[^A-Za-z0-9\s]+', '', sampleRead) #removes symbols

#splits string into list by word
sampleSplit = sampleReadClean.split() 
termSplit = termRead.split()

#counts all the occurrences of each word in term file from the text file.

for x in termSplit:
	print x
	termCount = sampleSplit.count(x)
	print "There are %i occurrences of the character %s in this section." %(termCount, x)


print enumerate(sampleSplit)

for x in termSplit:
	for i, j in enumerate(sampleSplit):
		if j == x:
			print i,j


##manually enter the word to split
#word = str(raw_input("Please enter a word to count:")) 
##this counts the number of occurances of the word.  
#print 'There are %d occurances of the word %s ' % (wordNum, searchWord)

sampleText.close()


