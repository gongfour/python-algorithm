
n = int(input())
for i in range(n):
    s = input()
    for c in s:
        if c.isupper():
            print(c.lower(), end='')
        else:
            print(c, end='')
    print()
