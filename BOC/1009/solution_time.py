t = int(input())
s = ''

for _ in range(t):
    a, b = map(int, input().split(" "))
    n = a
    cycle = []
    while(1):
        if(n%10) in cycle:
            break
        cycle.append(n%10)
        n = (n%10)*a
    if cycle[b % len(cycle) -1] == 0: s += f'{10}\n'
    else: s += f'{cycle[b % len(cycle) -1]}\n'

print(s[:-1])