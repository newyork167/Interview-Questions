hr_print <- function(n, x, p){
    write(round(1 - pbinom(x, n, p), 3), stdout())
}

p = 0.8

hr_print(4, 2, p)
hr_print(4, 2, 1-p)