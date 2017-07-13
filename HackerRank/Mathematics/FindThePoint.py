for case in [[j for j in input().split(' ')] for i in range(int(input().strip()))]:
    px, py, qx, qy = [int(x) for x in case[0:5]]
    print(qx + qx - px, qy + qy - py)
