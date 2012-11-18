library(pander)

results <- list()
results[['mtcars']] <- pandoc.table.return(mtcars)
results[['ks-test']] <- pander.return(ks.test(runif(50), runif(50)))

png("plot.png")
plot(runif(50), runif(50), pch=19, col="purple")
dev.off()

library(rjson)

storage <- file("storage.json", "w")
writeLines(toJSON(results), storage)
close(storage)
