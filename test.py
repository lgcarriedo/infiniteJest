#!/usr/bin/python

# # from the end of the string
# last_toe = "and _this_ little piggy went wee wee wee all the way home"
# # when given a second argument, reverse split counts
# list_from_string = last_toe.split(' ')

# print list_from_string

rhyme = '''There was a crooked man
Who walked a crooked mile.
He found a crooked sixpence
Against a crooked stile.
He bought a crooked cat
Which caught a crooked mouse,
And they all lived together
In a crooked little house.'''
 
# you can split on words as well as single letters and symbols
split_list = rhyme.split('.',1)
 
print "List output:"
for item in split_list:
     print item
print
partition_list = rhyme.partition('crooked')
print "Partition output:" #Partition does not take the "splitter" out. 
for item in partition_list:
     print item