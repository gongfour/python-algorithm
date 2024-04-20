
n = int(input())
rgb = []
for _ in range(n):
    rgb.append(tuple(map(int, input().split(' '))))
    
RG = [0] * n
RB = [0] * n
RR = [0] * n
RG[1] = rgb[0][0] + rgb[1][1]
RB[1] = rgb[0][0] + rgb[1][2]
RR[1] = 20001
GR = [0] * n
GB = [0] * n
GG = [0] * n
GR[1] = rgb[0][1] + rgb[1][0]
GB[1] = rgb[0][1] + rgb[1][2]
GG[1] = 2001
BR = [0] * n
BG = [0] * n
BB = [0] * n
BR[1] = rgb[0][2] + rgb[1][0]
BG[1] = rgb[0][2] + rgb[1][1]
BB[1] = 2001


# RG: RB + rgb[i][2]
# RB: RG + rgb[i][1]

# GB: GR + rgb[i][0]
# GR: GB + rgb[i][2]

# BG: BR + rgb[i][0]
# BR: BG + rgb[i][1]

for i in range(2, n):
    RG[i] = min(RB[i-1] + rgb[i][1], RR[i-1] + rgb[i][1]) # G
    RB[i] = min(RG[i-1] + rgb[i][2], RR[i-1] + rgb[i][2]) # B
    RR[i] = min(RB[i-1] + rgb[i][0], RG[i-1] + rgb[i][0])
    GB[i] = min(GR[i-1] + rgb[i][2], GG[i-1] + rgb[i][2]) # B
    GR[i] = min(GB[i-1] + rgb[i][0], GG[i-1] + rgb[i][0]) # R
    GG[i] = min(GR[i-1] + rgb[i][1], GB[i-1] + rgb[i][1])
    BR[i] = min(BG[i-1] + rgb[i][0], BB[i-1] + rgb[i][0]) # R
    BG[i] = min(BR[i-1] + rgb[i][1], BB[i-1] + rgb[i][1]) # G
    BB[i] = min(BR[i-1] + rgb[i][2], BG[i-1] + rgb[i][2])
    # print(rgb[i])
    
# print(f"RG = {RG}")
# print(f"RB = {RB}")
# print(f"GB = {GB}")
# print(f"GR = {GR}")
# print(f"BR = {BR}")
# print(f"BG = {BG}")

ans_r = min(RG[-1], RB[-1])
ans_b = min(BG[-1], BR[-1])
ans_g = min(GR[-1], GB[-1])
ans = min(min(ans_r, ans_b), ans_g)

print(ans)
