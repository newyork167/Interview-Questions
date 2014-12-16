def makeStringFromList(strList):
	returnStr = ""
	
	for x in strList:
		returnStr += x + " "
	
	return returnStr
	
file = open("output.txt", "w")

cases = int(input())

for case in range(0, cases):
	inStrList = input().split(' ')
	
	for xPos in range(0, int(len(inStrList) / 2)):
		temp = inStrList[xPos]
		inStrList[xPos] = inStrList[len(inStrList) - 1 - xPos]
		inStrList[len(inStrList) - 1 - xPos] = temp
	
	print("Case #" + str(case + 1) + ": " + makeStringFromList(inStrList))
	file.write("Case #" + str(case + 1) + ": " + makeStringFromList(inStrList) + "\n")
	
file.close()