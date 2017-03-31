u = 20
sd = 2

s = pnorm(19.5, mean=u, sd=sd)
write(round(s,3), stdout())
s = pnorm(22, mean=u, sd=sd) - pnorm(20, mean=u, sd=sd)
write(round(s,3), stdout())