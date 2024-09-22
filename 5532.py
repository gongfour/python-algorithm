import math

n = int(input())
a = float(input())
b = float(input())

aa = float(input())
bb = float(input())

na = math.ceil(a / aa)
nb = math.ceil(b / bb)

nn = max(na, nb)
print(n - nn)


