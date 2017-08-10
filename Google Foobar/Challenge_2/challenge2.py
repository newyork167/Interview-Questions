def answer(x, y):
    a = x * (x + 1) / 2
    for n in range(2, y + 1):
        a += x + n - 2
    return a

