ijdata <- read.csv("parserData.csv") 

ijdata$height <- 1

head(ijdata)

ggplot(ijdata, aes(postition, height, color = term)) + geom_point(position = "jitter")