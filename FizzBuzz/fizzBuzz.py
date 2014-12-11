def fizzBuzz():
	for x in range(1,101):
        fizzBuzz = ""
		
		fizzBuzz += "fizz" if x % 3 == 0
		fizzBuzz += "buzz" if x % 5 == 0
		
        if len(fizzBuzz) != 0:
            print(fizzBuzz)
		else:
			print(x)
			
fizzBuzz()