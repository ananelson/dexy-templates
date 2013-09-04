library(RSQLite)
library(Hmisc)

dexy.root <- Sys.getenv("DEXY_ROOT")
db.file <- file.path(dexy.root, "example_com/example.sqlite3")

con <- dbConnect(SQLite(), db.file)
png("plot.png", width=640, height=400)

### "query"
v <- fetch(dbSendQuery(con, "select * from polls_choice"))
dotchart(v$votes, labels=v$choice_text, pch=19, cex=1.5)
         

### "off"
dev.off()
