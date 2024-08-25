
n = int(input())
arr = list(map(int,input().split()))

count = 0
uphill_list = []
for i in range(n - 1):
    if arr[i + 1] > arr[i]:
        count += arr[i+1] - arr[i]
    else:
        count = 0
    uphill_list.append(count)
        
print(max(uphill_list))




