
import sys
n = int(sys.stdin.readline().rstrip())

sum = 0
for i in range(n):
    d = int(sys.stdin.readline().rstrip())
    sum += d
print(sum - (n - 1))

