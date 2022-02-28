
n = int(input())
num = []

for i in range(n):
    num.append(int(input()))

for i in range(n):
    temp = num[i]
    p = i
    for j in range(i, n):
        if temp > num[j]:
            temp = num[j]
            p = j
    num[i], num[p] = num[p], num[i]

for i in num:
    print(i)

