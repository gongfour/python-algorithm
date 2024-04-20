from math import factorial

n = int(input())
i = factorial(n)
i = str(i)

cnt = 0
for j, v in enumerate(i[::-1]):
    if v != '0':
        break
    cnt += 1 

print(cnt)
