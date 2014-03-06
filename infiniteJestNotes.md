#Infinite Jest

##Goal one:  Split and count

1. words
2. sentences
3. chapters
4. Paragraphs

##4. Paragraphs

    toes = '''went to the market
    stayed home
    had roast beef
    had none
    cried wee wee wee all the way home'''
     
    # splitlines splits on linebreaks
    list_from_string = toes.splitlines()
    print list_from_string
    for toe in list_from_string:
         print "this little piggy %s" % toe


##Some Ideas

I am going to need to make a hiearchy dictionary.  With Chapter, paragraph, sentence, word.  

Can I write in the text file and make it a variable right away?  


##Programing concepts

Here you are reading one line at a time. Could come in handy if you specify when to stop.  

    fh.readline()
    'YEAR OF THE DEPEND ADULT UNDERGARMENT \n'
    \>>> fh.readline(2)
    'Th'
    \>>> fh.readline(5)
    'ough '
    fh.readline(405)
    \>>> 'only one-half ethnic Arab and a Canadian by birth and residence, the medical attache is nevertheless once again under Saudi diplomatic immunity, this time as special ear-nose-throat consultant to the personal physician of Prince Q---------, the Saudi Minister of Home Entertainment, here on northeastern U.S.A. soil with his legation to cut another mammoth deal with 

Is what returns one variable that can be added to string?  What type of data is it.  How do you ask again?

    />>> isinstance(nextthirty,int);
    False
    />>> isinstance(nextthirty,basestring);
    True

You can assign it to a variable 

    />>> nextthirty = fh.readline(30)
    />>> nextthirty
    'l attache turns thirty-seven t'

If I continue reading line?  Does nextthirirty stay the same?  Should.

    \>>> nextForty = fh.readline(40)
    \>>> nextthirty
    'l attache turns thirty-seven t'
    \>>> nextForty

So we know it is part of the string. That means I can connect them together. If I can figure out how to cut them at every sentence (minus the acrynyms), Make a string of sentences in every paragraph. The key will be the paragraph and the value will be the string of sentences which belong to that paragraph. 

Many times it happens that we want to add more data to a value in a dictionary and if the key does not exists then we add some default value. You can do this efficiently using dict.setdefault(key, default). via [pymbook.readthedocs.org](http://pymbook.readthedocs.org/en/latest/datastructure.html#dictionaries)

    />>> data = {}
    />>> data.setdefault('names', []).append('Ruby')
    />>> data
    {'names': ['Ruby']}
    />>> data.setdefault('names', []).append('Python')
    />>> data
    {'names': ['Ruby', 'Python']}
    />>> data.setdefault('names', []).append('C')
    />>> data
    {'names': ['Ruby', 'Python', 'C']}
        'American lunar Y.D.A.U. The legation fin'


