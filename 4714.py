
while True:
    n = float(input())
    if n < 0:
        break
    moon_n = n * 0.167

    print(f'Objects weighing %.2f on Earth will weigh %.2f on the moon.' % (n, moon_n))
