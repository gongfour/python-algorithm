
n = int(input())

factor = 10
while n>=factor:
    n = (n + factor // 2) // factor * factor
    factor *= 10

print(n)



