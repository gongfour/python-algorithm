
xn = int(input())
s = input().strip()
yn = len(s) // xn

arr: list[list] = [[0] * xn for _ in range(yn)]
for y in range(0, yn):
    for x in range(0, xn):
        if y % 2 == 0:
            arr[y][x] = s[y * xn + x]
        else:
            arr[y][xn - 1 - x] = s[y * xn + x]


for x in range(0, xn):
    for y in range(0, yn):
        print(arr[y][x], end='')




