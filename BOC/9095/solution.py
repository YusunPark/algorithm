from itertools import count


global list

list = [0]*12
s = ''

def sum(n):
    if n == 1: list[n] = 1
    if n == 2: list[n] = 2
    if n == 3: list[n] = 4
    if list[n] != 0:
        pass
    else:
        sum(n-1)
        sum(n-2)
        sum(n-3)
        list[n] = list[n-1] + list[n-2] + list[n-3]

for _ in range(int(input())):
    n = int(input())
    sum(n)
    s += str(list[n])+'\n'

print(s[:-1])