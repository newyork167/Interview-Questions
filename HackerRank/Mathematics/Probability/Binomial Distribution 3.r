hr_print <- function(n, x, p, f){
    if(f){
        write(round(1 - pbinom(x, n, p), 3), stdout())
    }
    else{
        write(round(pbinom(x, n, p), 3), stdout())
    }
}

p = 0.12
n = 10

hr_print(n, 2, p, 0)
hr_print(n, 1, p, 1)