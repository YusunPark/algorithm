n = int(input())
v = input()

a, b = 0, 0
for x in v :
    if x == 'A': a += 1
    else: b += 1

if a == b: print('Tie')
elif a > b: print('A')
else: print('B')