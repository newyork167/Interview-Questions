n = int(input())
k = int(input())

nums = []

for x in range(0, n):
    nums.append(int(input()))

sortedNums = sorted(nums)
difference = sortedNums[n-1]

for x in range(0, n - k):
    xDifference = sortedNums[x+k-1] - sortedNums[x]
    difference = xDifference if xDifference < difference else difference
    
print(difference)