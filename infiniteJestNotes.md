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
