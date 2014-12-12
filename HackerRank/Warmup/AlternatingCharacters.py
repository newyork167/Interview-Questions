cases = 1

def remove(str, pos):
	return str[:pos] + str[pos+1:]

for case in range(0, cases):
	count = 0
	string = "AABBABABB"
	x = 0
	y = len(string)
	while x < y:
		while(x + 1 < y and string[x] == string[x+1]):
			string = remove(string, x+1)
			y -= 1
			count += 1
		x += 1
	print(count)