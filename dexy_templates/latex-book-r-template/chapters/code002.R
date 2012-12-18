data(iris)
library(xtable)
x <- xtable(iris[1:10,])
print(x, file="iris-table.tex")

