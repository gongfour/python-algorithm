from decimal import *
getcontext().prec = 100
L = Decimal('-1000000')
H = Decimal('1000000')

tor = Decimal('1e-50')

for _ in range(int(input())):
  a, b, c, d = map(Decimal, input().split())

  def fn(x):
    return a*x**3+b*x**2+c*x+d

  def binary(l, h):
    while h-l > tor:
      x = (l+h)/2
      if fn(x)*fn(l) > 0:
        l = x
      else:
        h = x
    return l

  if b**2-3*a*c < 0:  # 실근이 1개
    ans = [binary(L, H)]
  else:
    s1, s2 = sorted([(-b-(b**2-3*a*c)**Decimal('0.5'))/(3*a), (-b+(b**2-3*a*c)**Decimal('0.5'))/(3*a)])

    if round(fn(s1)*fn(s2), 20) > 0:  # 실근이 1
      ans = [binary(L, H)]
    elif round(fn(s1), 20) == 0 or round(fn(s2), 20) == 0:
      # 실근이 2개
      if round(fn(s1), 20) == 0:
        if round(s1, 20) == round(s2, 20):
          ans = [s1]
        else:
          ans = [s1, binary(s2, H)]
      else:
        ans = [binary(L, s1), s2]
    else:  # 실근이 3개
      ans = [binary(L, s1), binary(s1, s2), binary(s2, H)]

    ans = ['{:.20f}'.format(i) for i in ans]
    print(*ans)
