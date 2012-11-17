### @export "assign-variables"
x <- 6
y <- 7

### @export "multiply"
x * y

### @export "graph-name"
pdf("dexy--plot.pdf", width=6,height=4)

### @export "graph"
plot(c(1,2,3), pch=19, col="purple")

### @export "close-graph"
dev.off()

