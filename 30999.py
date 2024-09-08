
n, m = map(int, input().split())

count = 0
for _ in range(n):
    votes = input()
    sum = 0
    for v in votes:
        if v == 'O':
            sum += 1
    if sum > m//2:
        count += 1

print(count)


