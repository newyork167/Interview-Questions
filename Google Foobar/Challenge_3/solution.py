"""
foobar:~/hey-i-already-did-that newyork167$ status
Current level: 2
Challenges left to complete level: 1

Level 1: 100% [==========================================]
Level 2:  50% [=====================.....................]
Level 3:   0% [..........................................]
Level 4:   0% [..........................................]
Level 5:   0% [..........................................]

foobar:~/hey-i-already-did-that newyork167$ cat solution.py 
def​ ​solution(n,​ ​b):
​ ​​ ​​ ​​ ​#Your​ ​code​ ​here
"""

# TODO: Convert to python 2.7 because Google

def solution(n, b):
    minions = {}
    k = len(n)

    while True:
        minions[n] = minions.get(n, 0) + 1

        if minions[n] >= 3:
            return 1 + sum(map((2).__eq__, minions.values()))
        
        y = "".join(sorted(n))
        x = y[::-1]

        z = int(x, b) - int(y, b)

        # From https://stackoverflow.com/questions/2267362/how-to-convert-an-integer-to-a-string-in-any-base
        if z != 0:
            digits = []
            while z:
                digits.append(int(z % b))
                z //= b
            z = "".join(map(str, digits[::-1]))

        z = str(z).zfill(k)

        n = z

if __name__ == '__main__':
    to_solve = [
        ('1211', 10),
        ('210022', 3)
    ]

    for i, solve in enumerate(to_solve):
        print(f"Solution {i}: {solution(solve[0], solve[1])}")
