#infinitejestggplot.r
#Author: Ciera Martinez
#Plot character occurance by postion in book.
#There are two dataframes used to make this visualization, 
#1. Chapter Position (used to delinate chapter structuring)
#2. Character Postion 

#Required Libraries
library(ggplot2)
library(dplyr)

#1. Chapter Position
# read in ch.parser.py output
chapPos <- read.csv("../data/pyOutputs/chapterPosition.csv")
chapPos[65,1] <- "endnotes" #rename endnotes (last row)

#need to clean up position
chapPos$chapter <- gsub("<", "", chapPos$chapter)
chapPos$chapter <- gsub(">", "", chapPos$chapter)
chapPos$chapter <- gsub(" ", "", chapPos$chapter)


#to get chapter range
#make new vector independently of chapPos dataframe

#essentially removing first instance in vector and replacing last
#instance with NA, so row #'s stays the same. (to-do re-do with loop)
pos2 <- (chapPos$position - 1)
pos2 <- pos2[-1] 
pos2[65] <- NA #add a NA at the end so vector is length of chapPos rows
chapPos$position2 <- pos2 #bring back

#2. Character Postion 
#To get characterPosition.txt I ran ch.parser.py
charPos <- read.csv("../data/pyOutputs/characterPosition.csv")

#first deal with endnotes
chapPos[65,3] <- max(charPos$position)
#length column
chapPos$length <- (chapPos$position2 - chapPos$position)

#Now add a chapter column to specify where is each character position

# order the first data.frame by the ranges
chapPos <- chapPos[order(chapPos[[2]]), ]

# create a vector that breaks from the interval ranges
breaks <- as.vector(do.call(rbind, chapPos[c(2,3)]))
breaks
ints <- ceiling(findInterval(charPos[[2]], breaks)/2)

charPos$chp <- chapPos[ints, 1]

#Visualization 1
#Quickly just get a sense for how many times a character is mentioned
ggplot(charPos, aes(term)) +
  geom_bar(stat = "bin") +
  coord_flip() +
  theme_bw() +
  theme(text = element_text(),
        axis.text.x = element_text(angle=90, 
                                   vjust=1)) 

#Visualization 2
#Now I want to see the distribution 

#First get rectangles for chapter delimiters for the chapter graph at the bottom.
rect_left <- chapPos[['position']]
rect_left

rect_right <- chapPos[['length']]
rect_right

rect_right
rectangles <- data.frame(
  xmin = rect_left,
  xmax = rect_left + (rect_right - 500),
  ymin = 0,
  ymax = .5
)

ggplot() + 
	geom_point(
		data = charPos, 
		aes(x = position, y = term, color = chp))	+
	geom_rect(
		data = rectangles, 
		aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), 
		  fill = 'blue', 
		  alpha = .4) +
    ylab("") + 
  	xlab("") +
    theme_bw()

##Subset by chapter just to see
head(charPos)

#There is a space inserted after ch01, (to-do get rid of)
chapter7 <- subset(charPos, charPos$chp == "ch07") 
chapter7







