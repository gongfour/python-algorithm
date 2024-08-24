
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))
    arr = [i for i in arr if i % 2 == 0]
    sum_value = sum(arr)
    min_elem = min(arr)
    print(sum_value, min_elem)
