from collections import Counter

def answer(data, n):
	print ([x for x in data if Counter(data)[x] <= n])

# data = [1,1,2,5,3,3,4,7,7,6,6,6,9]
# n = 2
#
# answer(data=data, n=n)