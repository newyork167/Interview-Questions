# From Google Code Jam - Qual Round Africa 2010
# https://code.google.com/codejam/contest/351101/dashboard#s=p0

cases = int(input())

text_file = open("output.txt", "w")

for case in range(0, cases):
	c = int(input())
	i = int(input())
	l = []
	
	for x in input().split(' '):
		l.append(int(x))
	
	count = []
	
	for x in range(0, len(l)):
		if l[x] < c and len(count) == 0:
			for y in range(0, len(l)):
				if l[x] + l[y] == c and x != y:
					count.append(x)
					count.append(y)
	
	print("Case #" + str(case + 1) + ": " + str(count[0]) + " " + str(count[1]))
	text_file.write("Case #" + str(case) + ": " + str(count[0] + 1) + " " + str(count[1] + 1) + "\n")
text_file.close()