def fizzBuzz():
	for x in range(1,101):
		fizz = False #multiples of 3
		buzz = False #multiples of 5
		
		fizz = x % 3 == 0
		buzz = x % 5 == 0
		
		if fizz and buzz:
			
			print("fizzbuzz")
		elif fizz:
			print("fizz")
		elif buzz:
			print("buzz")
		else:
			print(x)
			
fizzBuzz()