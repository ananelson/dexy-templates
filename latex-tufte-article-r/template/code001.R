### @export "assign-variables"
x <- 5
y <- 7

### @export "multiply"
x * y
### @end

pdf("dexy--plot.pdf")
### @export "graph"
plot(c(1,2,3), pch=19, col="purple")
### @end
dev.off()

