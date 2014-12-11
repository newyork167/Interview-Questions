import time

def chop(x, intArray):
	mini = 0
	maxi = len(intArray) - 1
	
	while(True):
		y = (mini + maxi) // 2
		
		if(mini > maxi):
			return -1
		if(intArray[y] > x):
			maxi = y
		elif(intArray[y] < x):
			mini = y
		else:
			return y
		
		time.sleep(1)
			

print(chop(4, [1,2,3,4,5,6]))