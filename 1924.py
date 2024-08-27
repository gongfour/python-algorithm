

def days(m, d) -> int:
    if m == 1:
        return d
    elif m == 2:
        return 31 + d
    elif m == 3:
        return 59 + d
    elif m == 4:
        return 90 + d
    elif m == 5:
        return 120 + d
    elif m == 6:
        return 151 + d
    elif m == 7:
        return 181 + d
    elif m == 8:
        return 212 + d
    elif m == 9:
        return 243 + d
    elif m == 10:
        return 273 + d
    elif m == 11:
        return 304 + d
    elif m == 12:
        return 334 + d
    else:
        return 0


x, y = map(int, input().split())
d = days(x, y)

if d % 7 == 1:
    print("MON")
elif d % 7 == 2:
    print("TUE")
elif d % 7 == 3:
    print("WED")
elif d % 7 == 4:
    print("THU")
elif d % 7 == 5:
    print("FRI")
elif d % 7 == 6:
    print("SAT")
else:
    print("SUN")

