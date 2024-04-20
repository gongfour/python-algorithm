import math
from decimal import *
getcontext().prec=100

cnt = int(input())
L = Decimal('-1000000')
H = Decimal('1000000')

tor = Decimal('1e-10')

while cnt > 0:
    cnt -= 1
    
    a, b, c, d = map(Decimal, input().split())
    e, f, g = Decimal('3') * a, Decimal('2') * b, c

    def fn(x):
        return a * x*x*x + b * x*x + c * x + d

    def det(a, b, c):
        return b * b - Decimal('4') * a * c

    def sol_eq2(a,b,c):
        d = det(a,b,c)
        s1 = (-b - d.sqrt()) / 2 / a
        s2 = (-b + d.sqrt()) / 2 / a
        return sorted([s1 , s2])

    def sol_eq3(l, h):
        while True:
            if h - l < 10**-15:
                break
            x = (l+h)/2
            if fn(x)*fn(l) > 0:
                l = x
            else:
                h = x
        return x

    D = det(e,f,g)
    s1, s2 = Decimal('0'), Decimal('0')
    n = 0 # 실근의 개수
    if D < 0: # 실근 2개 -> 기울기가 0인 지점이 2개
        print(sol_eq3(L, H))
    else:
        s1, s2 = sol_eq2(e, f, g)
        if round(fn(s1) * fn(s2), 20) > 0: # 실근 1개
            print(sol_eq3(L, H))
        elif round(fn(s1),20) == 0 and round(fn(s2),20) == 0: # 3 중근
            print(s1) 
        elif round(fn(s1),20) == 0 or round(fn(s2), 20) == 0: # 2 중근
            if round(fn(s1), 20) == 0:
                print(s1, sol_eq3(s2, H))
            else:
                print(sol_eq3(L, s1), s2)
        else: # 실근 3개
            print(sol_eq3(L, s1), sol_eq3(s1,s2), sol_eq3(s2, H))
