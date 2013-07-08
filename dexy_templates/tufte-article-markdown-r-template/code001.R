### @export "assign-variables"
x <- 6
y <- 7

### @export "multiply"
x * y
### @end

pdf("plot.pdf")
### @export "graph"
plot(c(1,2,4), pch=19, col="purple")
### @end
dev.off()

