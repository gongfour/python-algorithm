
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

def ccw(x1, y1, x2, y2, x3, y3):
    t = (x1*y2+x2*y3+x3*y1) - (x2*y1+x3*y2+x1*y3)
    if t > 0: return 1
    elif t == 0: return 0
    else: return -1
    
p123 = ccw(x1, y1, x2, y2, x3, y3)
p124 = ccw(x1, y1, x2, y2, x4, y4)
p341 = ccw(x3, y3, x4, y4, x1, y1)
p342 = ccw(x3, y3, x4, y4, x2, y2)

ans = 0

# 양방향에서 CCW를 만족할 때 (가장 흔한 경우)
if p123 * p124 <= 0 and p341 * p342 <= 0: 
    if p123 * p124 == 0 and p341 * p342 == 0: # 점이 일직선 상에 존재
        b1 = max(x1,x2) >= min(x3,x4)
        b2 = max(x3,x4) >= min(x1,x2)
        b3 = max(y1,y2) >= min(y3,y4)
        b4 = max(y3,y4) >= min(y1,y2)
        if b1 and b2 and b3 and b4:
            ans = 1
    else:
        ans = 1

print(ans)