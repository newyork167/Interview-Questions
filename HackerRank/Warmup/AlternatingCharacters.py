cases = 1

def remove(str, pos):
	return str[:pos] + str[pos+1:]

for case in range(0, cases):
	count = 0
	string = input()
	points = []
	x = 0
	y = len(string)
	
	# New code runs in O(n + m) much better than the O(nm)
	for x in range(0, y):
		if x + 1 < y and string[x] == string[x+1]:
			points.append(x)
			count += 1
	
	for point in points:
		string = string[:point] + string[(point+1):]
	
	
	# Initial attempt runs in O(nm) failing one of the tests due to timeout
	#while x < y:
	#	while(x + 1 < y and string[x] == string[x+1]):
	#		string = remove(string, x+1)
	#		y -= 1
	#		count += 1
	#	x += 1
	print(count)