def treeGrowth(curHeight, count, double):
    if count == 0:
        return curHeight
    if double == True:
        return treeGrowth(2*curHeight, count - 1, False)
    else:
        return treeGrowth(curHeight + 1, count - 1, True)
        
        
cases = int(input())

for case in range(0,cases):
    count = int(input())
    print(treeGrowth(1, count, True))