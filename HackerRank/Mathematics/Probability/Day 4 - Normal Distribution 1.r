u = 30
sd = 4

x1 = 40
x2 = 21
x3 = 30
x4 = 35

write(round(pnorm(x1, u, sd), 3), stdout())
write(round(1 - pnorm(x2, u, sd), 3), stdout())
write(round(pnorm(x4, u, sd) - pnorm(30, u, sd), 3), stdout())