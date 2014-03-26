#Inifite Jest Project

I have two data files.  1. chapter position information. 2. character posisition character. I need to put them together. 

Read in the files


```r
chapPos <- read.table("chapterPosition.txt", header = TRUE)
charPos <- read.table("characterPosition.txt", header = TRUE)
```


Check those datasets out.


```r

head(chapPos)
head(charPos)
```


Results of Yesterdays Box Plots
=========
  
**Imani Bunn**


```r
p <- ggplot(stereotypes, aes(population, coffee, fill = gender))
```

```
Error: could not find function "ggplot"
```


```r
p + geom_boxplot(outlier.colour = "purple", outlier.size = 3, outlier.shape = 16, 
    aes(fill = population))
```

```
Error: object 'p' not found
```

*I changed "color" to colour to make the outlier purple identifier.  Those British.

**Kanyee Yang**


```r
ggplot(stereotypes, aes(beer, tacos, color = population, shape = gender)) + 
    geom_boxplot()
```

```
Error: could not find function "ggplot"
```


**Alex Furguson**


