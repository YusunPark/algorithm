# 시간초과

n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

count = n

for x in a:
    value = x-b
    if (value % c == 0) : count += value//c
    else : count += (value // c )+1

print(count)