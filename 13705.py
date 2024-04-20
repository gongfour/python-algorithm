import math
from decimal import *

getcontext().prec = 50
getcontext().rounding = ROUND_HALF_UP

pi = Decimal('3.14159265358979323846264338327950288419716939937510')

a, b, c = input().split()
a = Decimal(a)
b = Decimal(b)
c = Decimal(c)

# print(a,b,c)

def decimal_sin(x):
    x = x % (Decimal('2') * pi)
    i = Decimal('1') # 1, 3, 5, 7 ...
    lasts = Decimal('0')
    value = Decimal(x)
    fact = Decimal('1')
    num = Decimal(x)
    sign = Decimal(1)
    while value != lasts:
        lasts = value
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        value += num / fact * sign
    return Decimal(value)

def decimal_cos(x):
    x = x % (Decimal('2') * pi)
    i = Decimal('0') # 0, 2, 4, 8 ...
    lasts = Decimal('0')
    value = Decimal('1')
    fact = Decimal('1')
    num = Decimal(x)
    sign = Decimal(1)
    while value != lasts:
        lasts = value
        i += 2
        fact *= i * (i-1)
        num *= x * x
        sign *= -1
        value += num / fact * sign
    return Decimal(value)

def func(x) -> float:
    return a * x + b * decimal_sin(x) - c

def derivative(x) -> float:
    return a + b * decimal_cos(x)

left = c / a - Decimal('1')
right = c / b + Decimal('1')

while right - left > Decimal(1e-20):
    mid = (left + right) / 2
    if func(mid) > 0:
        right = mid
    elif func(mid) < 0:
        left = mid
    else:
        break

ans = (left + right) / 2
print(round(ans, 6))