
n = input().rstrip()
d = list(input().rstrip().split())

count = 0
for i in d:
    if i == n:
        count += 1

print(count)
