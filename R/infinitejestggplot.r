library(ggplot2)

chapPos <- read.table("../data/chapterPosition.txt", header = TRUE)
charPos <- read.table("../data/characterPosition.txt", header = TRUE)

#I need to combine them together. Using information from chapPos. Or do I?

head(chapPos)
head(charPos)

tail(charPos)
tail(chapPos)

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

ggplot() + 
	geom_point(
		data = charPos, 
		aes(x = position, y = term ) #need to fill on group. Arrange by group. 
	)	+
	geom_rect(
		data = rectangles, 
		aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), 
		fill = 'blue', 
		alpha = .7) +
  		ylab("") + 
  		xlab("")
  



