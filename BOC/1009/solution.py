t = int(input())
s = ''


for _ in range(t):
    a, b = map(int, input().split(" "))
    if a**b%10 == 0: s += f'{10}\n'
    else: s += f'{a**b%10}\n'

print(s[:-1])