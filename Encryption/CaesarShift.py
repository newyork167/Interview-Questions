import sys

def CaesarShift(string, inc):
	newString = ""
	
	if inc < 0:
		inc = 26 - (-inc % 30)
	elif inc > 26:
		inc = inc % 26
	
	for x in string:
		y = ord(x) + inc
		if y >= 91 and (y - inc) <= 91 :
			y = 65 + (y - 91)
		elif y >= 123:
			y = 97 + (y - 123)
		newString += chr(y)
	return newString
	
if len(sys.argv) != 3:
	print("USAGE: " + sys.argv[0] + " {input string} {int to shift by}")
else:
	print(CaesarShift(sys.argv[1], int(sys.argv[2])))