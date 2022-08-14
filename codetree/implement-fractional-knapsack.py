n, m = map(int, input().split())

jewel = []

for _ in range(n):
    w, v = map(int, input().split())
    jewel.append([v/w, w])

jewel.sort(reverse = True)

result = 0
for val, count in jewel:
    if m == 0:
        break
    elif m >= count:
        result += (val*count)
        m -= count
    else:
        # m < count
        result += (val*m)
        m = 0


# result = 0
# for i in range(m):
#     result += jewel[i]

print(f"{result:.3f}")