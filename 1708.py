
def ccw_raw(x1, y1, x2, y2, x3, y3):
    return x1*y2+x2*y3+x3*y1 - x2*y1+x3*y2+x1*y3
    
def ccw(p1, p2, p3):
    return ccw_raw(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
    
n = int(input())
pts = list()
for _ in range(n):
    x, y = map(int, input().split())
    pts.append((y,x))

pts.sort()
pts[1:].sort(key=lambda p1, p2: ccw(pts[0], p1, p2))

print(pts)




    