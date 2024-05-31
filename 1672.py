n = int(input())
d = list(input())

map = {
    'AA' : 'A',
    'AG' : 'C',
    'AC' : 'A',
    'AT' : 'G',
    'GA' : 'C',
    'GG' : 'G',
    'GC' : 'T',
    'GT' : 'A',
    'CA' : 'A',
    'CG' : 'T',
    'CC' : 'C',
    'CT' : 'G',
    'TA' : 'G',
    'TG' : 'A',
    'TC' : 'G',
    'TT' : 'T'
}

for i in range(n-2, -1, -1):
    d[i] = map[d[i] + d[i + 1]]
    d[i + 1] = "" 

print(d[0])
