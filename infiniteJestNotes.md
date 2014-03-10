#Infinite Jest

##Goal one:  Split and count

1. words
2. sentences
3. chapters
4. Paragraphs

##1. wordParser.py

There are so 
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


#Order on how created the project

1.  I first started messing with a small sample file, that I could manage a bit easier. 
2.  I then started looking into how to do simple tasks like splitting into more digestible sections using the split() method.
3.  In order to understand the output of the splitting I was doing I brushed up on understanding Python data stuctures, using the [best written guide to any programing I had ever seen](http://pymbook.readthedocs.org/en/latest/datastructure.html#matrixmul-py).  
4. I wanted to count something super simple, like words, so I wrote a little program that asks for the word, then prints the number of occurances of that word. This also goes along with one of my long term goals of being able to count all the character/terms and there location relative to book. 

There are several reasons why splitting using ```wordSplit = sampleRead.split()``` doesn't work. Since it is cutting on the space all the symbols are present. 

5.  Do I even need to split into list to get occurances? It might be easier to leave as string, remove symbols, and use the find feature. 

###TODOD NEXT



**Get list of Characters**

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

**You can lists within lists.** via [pymbook.readthedocs.org](http://pymbook.readthedocs.org/en/latest/datastructure.html#dictionaries)

    />>> a
    [45, 43624356, -3434, 1, 45, 23, 1, 111, [45, 56, 90]]
    />>> a[-1]
    [45, 56, 90]


**find() method for a string**

If it matches to more than one, it will reply ```0```

    />>> a
    'for for fight for but there'
    />>> a.find("for")
    0
    />>> a.find("fight")
    8

##Data Mining the internet with Python

**Resource*** [How to Mine the Web](http://www.whosbacon.com/how-to-mine-the-web)

You will need three main things

1. HTTP client.  The first step is to gather all of the content and make it in a readible form.

good option [Requests: HTTP for Humans](http://docs.python-requests.org/en/latest/index.html)

2. Content Parsing.  Once you have the content, you can now parse the data. You can parse the text(HTML) by using a structual tranverser like [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) or pattern matching with Regex.  Pattern matching might be the easiest option for me.  I will have to look at the html. 

I just looked at the source.  And it should be pretty easy to just copy the source page for each page and use pattern matching for content between ```<b></b>``` tags.


