a, b, c = map(int, input().split())

def power(a, b):
    if b == 1:
        return a % c
    if b % 2 == 0:
        d = power(a, b/2) % c
        return (d * d) % c
    else:
        d = power(a, (b-1)/2) % c
        return (d * d * a) % c
    
print(power(a,b))