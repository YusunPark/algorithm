import sys

n, m = map(int, input().split())

a = [
    list(map(str, input().split()))
    for _ in range(n)
]

b = [
    list(map(str, input().split()))
    for _ in range(m)
]

route_a = []
value_a = 0

route_b = []
value_b = 0

for d, v in a:
    for _ in range(int(v)):
        if d == 'R':
            value_a += 1
            route_a.append(value_a)
        else:
            value_a -= 1
            route_a.append(value_a)
for d, v in b:
    for _ in range(int(v)):
        if d == 'R':
            value_b += 1
            route_b.append(value_b)
        else:
            value_b-=1
            route_b.append(value_b)

time = 0
for i, j in zip(route_a, route_b):
    time += 1
    if i == j:
        print(time)
        sys.exit()


print(-1)
    
