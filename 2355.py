
def sum_upto(n):
    return n * (n + 1) // 2

a, b = tuple(map(int, input().split()))
if a > b:
    a, b = b, a
print(sum_upto(b) - sum_upto(a - 1))
