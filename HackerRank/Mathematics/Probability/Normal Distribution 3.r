u = 70
sd = 10

s = 1 - pnorm(80, mean=u, sd=sd, lower.tail=TRUE)
write(round(s * 100, 2), stdout())
s = pnorm(60, mean=u, sd=sd, lower.tail=FALSE)
write(round(s * 100, 2), stdout())
s = pnorm(60, mean=u, sd=sd, lower.tail=TRUE)
write(round(s * 100, 2), stdout())