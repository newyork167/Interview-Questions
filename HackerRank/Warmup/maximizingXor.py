#!/usr/bin/python3
def maxXor(l, r):
	biggest = 0;
	for x in range(l,r + 1):
		for y in range(x,r + 1):
			num = x ^ y
			if num >= biggest:
				biggest = num
	return biggest
        
if __name__ == '__main__':
	l = int(input())
	r = int(input())
	print(maxXor(l, r))