n = int(input())
f = int(input())

n = n - n % 100
ans = (f - n % f) % f
if ans == 0:
    print("00")
elif ans < 10:
    print("0" + str(ans))
else:
    print(ans)

