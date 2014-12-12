cases = int(input())

fibo = []

def searchFibo(x):
    if x in fibo:
        return True
    return False

def addToFibo(x):
    num1 = 1;
    num2 = 1;
    while(num2 <= x):
        newNum = num1 + num2
        if newNum not in fibo:
            fibo.append(newNum)
        if(num1 + num2 == x):
            return True
        if(num1 <= num2):
            num1 = newNum
        else:
            num2 = newNum
    return False

for case in range(0, cases):
    num = int(input())
    if searchFibo(num) == True or addToFibo(num):
        print("IsFibo")
    else:
        print("IsNotFibo")