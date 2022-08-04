n, m = map(int, input().split())

a = []
for _ in range(n):
    v, t = map(int, input().split())
    for _ in range(t):
        a.append(v)

b = []
for _ in range(m):
    v, t = map(int, input().split())
    for _ in range(t):
        b.append(v)

a_total = 0
b_total = 0

count = 0
first = ''

for i, j in zip(a, b):
    a_total += i
    b_total += j

    if a_total > b_total and first != 'a':
        count += 1
        first = 'a'
    
    elif b_total > a_total and first != 'b':
        count += 1
        first = 'b'
    
    else:
        pass

if count == 0:
    print(count)
else:
    print(count-1)
