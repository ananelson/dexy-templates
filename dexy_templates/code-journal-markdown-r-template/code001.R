### @export "assign-variables"
x <- 5
y <- 7

### @export "multiply"
x * y

### @export "graph"
png("plot.png")
plot(c(1,2,3), pch=20, col="purple")
dev.off()

