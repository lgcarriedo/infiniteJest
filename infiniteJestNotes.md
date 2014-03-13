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
4. I wanted to count something super simple, like words, so I wrote a little program that asks for the word, then prints the number of occurances of that word. This also goes along with one of my long term goals of being able to count all the character/terms and there location relative to book length. 

There are several reasons why splitting using ```wordSplit = sampleRead.split()``` doesn't work. Since it is cutting on the space all the symbols are present. 

5.  Do I even need to split into list to get occurances? It might be easier to leave as string, remove symbols, and use the find feature. No.  It is easiest to just remove symbols then make a list. The list will be useful later as I need an index number for each word. 

6. Then I made the program input the two files from command line, to help with testing. 

7.  Now I need to parse out each chapter. 

Parsing out each chapter is harder than I imagined.  I think what I need to do is to take advantage of the list of chapters and split by that list and reinterate over that list to split into list. 

Auctually I am going to save this for later.

8. I can go ahead and use my list of word and get counts and understand their index further.  Each word has it's position. 
    
    position = 
        a.) start of word found when searching through string
        b.) index number in list
            ex.  x from  termSplit 

You need to retrieve the index number of x in termSplit #x = term in terms.txt

The goal is to get a tab demlimited file to enter into R. 
Each row is 

print "%i (tab) %s (tab) %" %(termCount, x, (index#) )

1.  find tab
2.  find out how to find index number from item in string.  This will be the position. Find occurance print all postitions of occurance. Print x and **each** occurance on a new row. Each row signifies one occurance of what was found. 
3. use the ```find()``` function because it returns postion of first occurance.  But how do I find all occurances and postion?


list.index(x)
Return the index in the list of the first item whose value is x. It is an error if there is no such item.


\b[A-Z0-9]{2,}\b


###TODOD NEXT

Now I need to split each of these into chapters. 

Regex for a paragraph:  ^M

I then need to assign the number to each chapter.  

numWords per chapter = chapLen.

Each found term will be assigned a number based on chapter and overall in the book. 

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


**```find()``` method for a string**

If it matches to more than one, it will reply ```0```

    />>> a
    'for for fight for but there'
    />>> a.find("for")
    0
    />>> a.find("fight")
    8

**help**

    \>>> help(["foo", "bar", "baz"])
    Help on list object:

    class list(object)
    ...


    |
    |  index(...)
    |      L.index(value, [start, [stop]]) -> integer -- return first index of value
    |

**```enumerate()``` to get indexes of multiple if duplicates are in the list.

    for i, j in enumerate(['foo', 'bar', 'baz']):
        if j == 'bar':
            print i

##Data Mining the internet with Python

**Resource*** [How to Mine the Web](http://www.whosbacon.com/how-to-mine-the-web)

You will need three main things

1. HTTP client.  The first step is to gather all of the content and make it in a readible form.

good option [Requests: HTTP for Humans](http://docs.python-requests.org/en/latest/index.html)

2. Content Parsing.  Once you have the content, you can now parse the data. You can parse the text(HTML) by using a structual tranverser like [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) or pattern matching with Regex.  Pattern matching might be the easiest option for me.  I will have to look at the html. 

I just looked at the source.  And it should be pretty easy to just copy the source page for each page and use pattern matching for content between ```<b></b>``` tags.

##Notes on why in the project

I have been absorbing information on Python for about a year, but I never really built anything with it. I had an idea of data structure and syntax, but could never really find the motivation to build anything.  I think this is partly because all the programming I had to do, I could do in R, so I never really wanted to take the extra time to learn it.  Another problem is I am just so sick of DNA.  I am sick of the many combinations of four letters.  I love the bigger picture of bioinformatic analysis using sequencing data, but god is it boring to learn a language with.  

Then came an idea, that I had never thought before, I don't have to learn Python with sequencing data.  I don't have to learn all programming in the context of bioinformatics.  So what is a large plain text file I could use?  Yes. Infinite Jest.  Infinite Jest is a mamoth piece of beautifuly complex literature.  The world in Infinite Jest is deeply rooted in my heart, I love these words. I am not alone in this fasination, there are people all over the internet finding connections, making extensive notes, analyzing this text, but from my searches, no one has delved into the patterns. 
