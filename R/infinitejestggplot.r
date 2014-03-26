library(ggplot2)

chapPos <- read.table("chapterPosition.txt", header = TRUE)
charPos <- read.table("characterPosition.txt", header = TRUE)

#I need to combine them together. Using information from chapPos. Or do I?

# cellcounts$significance[cellcounts$p.value <= 0.0001] <- "0.0001"

head(chapPos)
head(charPos)

tail(charPos)
tail(chapPos)




#this is generating the data.
#dat <- data.frame(my_x_series=1:10000, #my_y_series=5.0*runif(192))



#in order for me to modify this I need convert a column (charPos$position1) to a numeric vector.  Try using this function:

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

head(rectangles)

ggplot() + 
	geom_point(
		data = charPos, 
		aes(x = position, y = term )#need to fill on group. Arrange by group. 
	)	+
	geom_rect(
		data = rectangles, 
		aes(xmin = xmin, xmax = xmax, ymin = ymin, ymax = ymax), 
		fill = 'blue', 
		alpha = .7) +
  		ylab("") + 
  		xlab("")
  



