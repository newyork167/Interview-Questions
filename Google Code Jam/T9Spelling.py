def returnNumberFromLetter(letter):
	num = 0
	presses = 0
	
	if letter == ' ':
		num = 0
		presses = 0
	elif ord(letter) - 97 < 18:
		num = int( (ord(letter) - 97) / 3 ) + 2
		presses = (ord(letter) - 97) % 3
	else:
		num = int( (ord(letter) - 95 ) / 3) + 1
		presses = (ord(letter) - 95) % 3
		if letter == 's':
			presses = 3
		elif letter == 'z':
			num -= 1
			presses = 3
	
	return [num, presses + 1]

cases = int(input())

file = open("output.txt", "w")

for case in range(0, cases):
	message = input()
	charList = ""
	
	for letter in message:
		result = returnNumberFromLetter(letter)
		if len(charList) > 0 and str(result[0]) == charList[len(charList) - 1]:
			charList += ' '
		charList += result[1]*str(result[0])
	file.write("Case #" + str(case + 1) + ": " + charList + "\n")