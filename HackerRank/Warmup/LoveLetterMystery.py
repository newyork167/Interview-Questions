cases = int(input())

for case in range(0, cases):
    string = input()
    count = 0
    
    for x in range(0, int(len(string)/2)):
        y = len(string) - 1 - x
        if string[x] != string[y]:
            if string[x] > string[y]:
                count += ord(string[x]) - ord(string[y])
            else:
                count += ord(string[y]) - ord(string[x])
    print(count)