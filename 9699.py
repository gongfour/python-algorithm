
n = int(input())
for i in range(n):
    a = list(map(int, input().split()))
    b = max(a)
    print(f'Case #{i+1}: {b}')
