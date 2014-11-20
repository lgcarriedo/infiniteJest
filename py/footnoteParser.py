#!/usr/bin/env python
#footnoteParser.py
#Lenoela

#This script takes in two arguments



#sample command to run (for infinite jest project)
#python py/footnoteParser.py data/bookText/David-Foster-Wallace-Infinite-Jest-v2.0.txt data/character/characters.mod.txt

import re
import sys	

#This sets up output file
#orig_stdout = sys.stdout
#data = open("./data/pyOutputs/characterPosition.txt", 'w')
#sys.stdout = data

#prints the headers of columns
print 'term\tposition\tfootnote\tstart\tend\tlength'


sampleText = open(sys.argv[1]) #file that contains text
listOfTerms = open(sys.argv[2]) #file that contains terms to search for

sampleRead = sampleText.read() #Makes one item string
termRead = listOfTerms.read()

termSplit = termRead.split("\r") #split by new line

#for term in termSplit:
	#for m in re.finditer(term, sampleRead):
		#print m.group(0), "\t", m.start()

#Outputs print
#sys.stdout = orig_stdout

#sampleText.close()
#listOfTerms.close()
#data.close()


#position of the footnote, outlined by the boundaries of
#extract the lenght of the footnotes

#\t makes a new column

#need to know the footnote number, and that is going to be "CharList" type of file that I will use to run in the for loop

