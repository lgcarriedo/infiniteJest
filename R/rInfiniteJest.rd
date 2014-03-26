#Inifite Jest Project

I have two data files.  1. chapter position information. 2. character posisition character. I need to put them together. 

Read in the files

```{r, comment="", results='hide',fig.cap=""}
chapPos <- read.table("chapterPosition.txt", header = TRUE)
charPos <- read.table("characterPosition.txt", header = TRUE)
```

Check those datasets out.

```{r, comment="", results='hide',fig.cap=""}
head(chapPos)
head(charPos)
```




