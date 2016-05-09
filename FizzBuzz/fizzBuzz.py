def fizzBuzz():
    for x in range(1,101):
		fizzBuzz = "fizz" if x % 3 == 0 else ""
		fizzBuzz += "buzz" if x % 5 == 0 else ""
		print(fizzBuzz if len(fizzBuzz) != 0 else x)

def fizzBuzz2():
    # For an implementation using list comprehension, hopefully a more compact will be coming soon
    ["fizzbuzz" if (x % 3 ==0 and x % 5 == 0) else "fizz" if x % 3 ==0 else "buzz" if x % 5 ==0 else x for x in range(1,101)]
			
fizzBuzz()
