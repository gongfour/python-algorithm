
while True:
    n = int(input())
    if n == 0:
        break
    arr = [] 
    for _ in range(n):
        string = input()
        arr.append((string.lower(), string))
    arr.sort()
    print(arr[0][1])

