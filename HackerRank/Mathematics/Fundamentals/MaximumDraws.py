cases = [[j for j in raw_input().split(' ')] for i in range(int(raw_input().strip()))]

[[print(int(x) + 1) for x in case[y]] for y in cases]