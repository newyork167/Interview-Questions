cases = int(input())

for x in range(0, int(cases)):
    in1 = int(input())
    temp = in1
    divisors = 0
    
    while temp != 0:
        y = temp % 10
        if x == 0:
            continue
        elif in1 % x == 0:
            divisors += 1
        temp = int(temp / 10)
    
    print(divisors)