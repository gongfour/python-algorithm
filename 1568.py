
n = int(input())
idx = 0
cnt = 0
answer = 0
while idx < n:
    cnt += 1
    idx += cnt
    if idx > n:
        idx -= cnt
        cnt = 0 
        answer -= 1
    answer += 1


print(answer)


