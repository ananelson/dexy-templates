### @export "assign-variables"
x <- 5
y <- 7

### @export "multiply"
x * y

### @export "graph"
pdf("dexy--plot.pdf")
plot(c(1,2,3), pch=19, col="purple")
dev.off()

