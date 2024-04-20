import math
a, b, c = map(int, input().split())

def func(x) -> float:
    return a * x + b * math.sin(x) - c

def derivative(x) -> float:
    return a + b * math.cos(x)

x = 19
while True:
    y_value = func(x)
    
    if abs(y_value) < 10 ** -9:
        break
    
    y_derivative = derivative(x)
    x = x - (y_value / y_derivative)
    
print(x)