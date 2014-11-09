#infinitejestggplot.r
#Author: Ciera Martinez
#Plot character occurance by postion in book.
#There are two dataframes used to make this visualization, 
#1. Chapter Position (used to delinate chapter structuring)
#2. Character Postion 

#Required Libraries
library(ggplot2)

# read in ch.parser.py output
chapPos <- read.csv("../data/pyOutputs/chapterPosition.csv")
head(chapPos)

#need to clean up position
chapPos$chapter <- gsub("<", "", chapPos$chapter)
chapPos$chapter <- gsub(">", "", chapPos$chapter)

#to get chapter range  (maybe a bit of a weird way)
#make new vector independently of chapPos dataframe

sample <- (chapPos$position - 1)

sample <- sample[-1] 
sample[65] <- NA #add a NA at the end so vector is length of chapPos rows
chapPos$position2 <- sample #bring back

#length column
chapPos$length <- (chapPos$position2 - chapPos$position)
head(chapPos)

#for the chapter graph at the bottom.
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

head(rectangles)
#To get characterPosition.txt I ran ch.parser.py
charPos <- read.csv("../data/pyOutputs/characterPosition.csv")

summary(charPos)

#In order to re-order by the total number of occurances, you need to get the 
#attach the total number of times that occurance happened.  

ggplot(charPos, aes(term)) +
  geom_bar(stat = "bin") +
  coord_flip() +
  theme_bw() +
  theme(text = element_text(),
        axis.text.x = element_text(angle=90, 
                                   vjust=1)) 

ggplot() + 
	geom_point(
		data = charPos, 
		aes(x = position, y = term))	+
	geom_rect(
		data = rectangles, 
		aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), 
		  fill = 'blue', 
		  alpha = .4) +
    ylab("") + 
  	xlab("") +
    theme_bw()

  



