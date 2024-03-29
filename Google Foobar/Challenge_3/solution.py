"""
foobar:~/hey-i-already-did-that newyork167$ status
Current level: 2
Challenges left to complete level: 1

Level 1: 100% [==========================================]
Level 2:  50% [=====================.....................]
Level 3:   0% [..........................................]
Level 4:   0% [..........................................]
Level 5:   0% [..........................................]
"""

# TODO: Convert to python 2.7 because Google

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return "".join(map(str, digits[::-1]))

def solution(n, b):
    minions = {}
    k = len(n)

    while True:
        minions[n] = minions.get(n, 0) + 1

        if minions[n] >= 3:
            twos = 0
            for i in minions.keys():
                if minions[i] == 2:
                    twos += 1
            return 1 + twos
        
        y = "".join(sorted(n))
        x = y[::-1]

        z = int(x, b) - int(y, b)

        # From https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
        z = numberToBase(z, b).zfill(k)

        n = z

if __name__ == '__main__':
    to_solve = [
        ('1211', 10),
        ('210022', 3)
    ]

    for i, solve in enumerate(to_solve):
        print("Solution " + str(i) + ": " + str(solution(solve[0], solve[1])))
