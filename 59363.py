import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

a.sort()
s = 0
for i in range(1, n):
    s += (a[i] - a[i-1]) * i * (n-i)

print(s * 2)
