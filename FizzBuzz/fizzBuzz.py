def fizzBuzz():
    for x in range(1,101):
		fizzBuzz = "fizz" if x % 3 == 0 else ""
		fizzBuzz += "buzz" if x % 5 == 0 else ""
		print(fizzBuzz if len(fizzBuzz) != 0 else x)
			
fizzBuzz()