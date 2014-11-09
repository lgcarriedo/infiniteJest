library(ggplot2)

#To get chapterPosition.txt, I ran ch.parser.py
chapPos <- read.table("../data/pyOutputs/chapterPosition.txt", header=TRUE)

#To get characterPosition.txt I ran ch.parser.py
charPos <- read.csv("../data/pyOutputs/characterPosition.csv")

summary(charPos)
#I need to combine them together. Using information from chapPos. Or do I?

#for the chapter graph at the bottom.
rect_left <- chapPos[['position1']]
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


#In order to re-order by the total number of occurances, you need to get the 
#attach the total number of times that occurance happened.  

ggplot() + 
	geom_point(
		data = charPos, 
		aes(x = term, y = postition))	+
	geom_rect(
		data = rectangles, 
		aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), 
		  fill = 'blue', 
		  alpha = .7) +
    ylab("") + 
  	xlab("") +
    theme_bw()
  



