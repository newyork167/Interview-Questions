hr_print <- function(n, x, p){
    write(round(1 - pbinom(x, n, p), 3), stdout())
}

p = 1.09 / (1.09 + 1)

hr_print(6, 2, p)