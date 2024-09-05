n = int(input())

people = {}
for i in range(n):
    person = input()
    p = person[0]
    people[p] = people.get(p, 0) + 1

found = False
for k, v in sorted(people.items()):
    if v >= 5:
        print(k, end='')
        found = True

if not found:
    print('PREDAJA')



