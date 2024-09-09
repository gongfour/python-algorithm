
w = float(input())
h = float(input())

bmi = w / (h * h)
if bmi < 18.5:
    print('Underweight')
elif bmi <= 25:
    print('Normal weight')
else:
    print('Overweight')

