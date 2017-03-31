f = [[], []]

for t in range(int(input())):
    a = list(map(int, input().split()))
    [f[x].append(a[x]) for x in range(len(a))]

print(min(f[0]) * min(f[1]))
