#!/usr/bin/env python
#parser.py
#Ciera Martinez

import re	

#These two lines read in the two data files. 
#The first be the file with the text and  
#list of terms to count the occurances of.

#It would be great to have these manually entered. 

sampleText = open('sample.txt')
listOfTerms = open('terms.txt')
 
sampleRead = sampleText.read() #makes a one item string
termRead = listOfTerms.read() 

#removes symbols, like all, even periods. 

sampleReadClean = re.sub('[^A-Za-z0-9\s]+', '', sampleRead)

sampleSplit = sampleReadClean.split() #makes a list
termSplit = termRead.split()

##Used this to test structure
# samplereadtype = type(sampleSplit)
# print "sampleRead is %s" % (samplereadtype)
# print type(sampleRead)

##manually enter the word to split
#word = str(raw_input("Please enter a word to count:")) 

#This is where I to put the loop.

n = len(termSplit)

print n

#for x in termSplit:

searchWord = termSplit[1]

wordNum = sampleSplit.count(searchWord) #this counts the number of occurances of the word.  

print 'There are %d occurances of the word %s ' % (wordNum, searchWord)

sampleText.close()


