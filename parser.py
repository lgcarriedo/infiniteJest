#!/usr/bin/env python
 
#Splits by word, although it is just splitting by space.  So if there is a
#symbol it is included in the "word".  I think I am going to have to be more explicit.

fh = open('sample.txt')
sample = fh.read()

wordSplit = sample.split(' ',1)

#print  wordSplit #prints the string

#view only the head of the file

head = wordSplit.readlines(4)
print head

with open("datafile") as myfile:
       head = myfile.readlines(N)
    print head

print wordSplit.count('.') #this counts the number of occurances of the word "the"

#This prints everything in the list on a new line
# for item in wordSplit:
#      print item

fh.close()

#Being more explicit
# split(str, num) 
# num = the # of lines made


