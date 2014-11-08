#!/usr/bin/env python
#parser.py This attaches postion number to word from a list of words.  Built to take in the chapter list and print out the position the chapter begins. 
#Ciera Martinez

#Working on: searching multiple word terms

#I think turning the whole book into one word terms 
#is the problem.  What I have to do just search the book 
#text.   

#What is the structure of what we read in?

import re
import sys	

#This sets up output file
#orig_stdout = sys.stdout
#data = open("parserData.txt", 'w')
#sys.stdout = data

#prints the headers of columns
#print 'postition\tterm'

sampleText = open(sys.argv[1]) #file that contains text

listOfTerms = open(sys.argv[2]) #file that contains terms to search for

sampleRead = sampleText.read() #Makes one item string
#print type(sampleRead)



termRead = listOfTerms.read() 

sampleReadClean = re.sub('[^A-Za-z0-9\s]+', '', sampleRead) #removes symbols

#splits string into list by word
sampleSplit = sampleReadClean.split() 
termSplit = termRead.split("\r") #split by new line

#I need termSplit to be a list of characters with space, split by new line or something

#Here is where I need to search throught the one item string instead of 
#splitting by word into a list, as done below.


#print re.findall("Hal", sampleRead) #Then it prints out all the Hal's, 

#If I could just search through the list of terms and have it print position.
#position will likely be character.

#Instead of printing a sting, I will print out postion 
#Nested loop.  

#for x in termSplit
	#for m in re.finditer("weed", sampleRead):
    	#print(m.group(0))
    	#print(m.start())

# That is basically it now format correctly 
#look into wht group does exactly


#for x in termSplit:
	#for i, j in enumerate(sampleSplit):
		#if j == x:
			#print '%i\t%s' % (i, j)

#Outputs print
#sys.stdout = orig_stdout

#sampleText.close()
#listOfTerms.close()
#data.close()


