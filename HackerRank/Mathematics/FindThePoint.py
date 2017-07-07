for case in [[j for j in raw_input().split(' ')] for i in range(int(raw_input().strip()))]:
	px, py, qx, qy = [int(x) for x in case[0:5]]
    print qx + qx - px, qy + qy - py