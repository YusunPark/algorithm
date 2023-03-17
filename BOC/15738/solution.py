import math

n, idx, m = map(int, input().split())
a = list(map(int, input().split()))

idx -= 1

for _ in range(m):
    num = int(input())

    if num > 0 and num > idx:
        idx += ((num-1)/2 - idx) * 2

    elif num < 0 and n+num < idx:


        idx += ((abs(num)-1)/2 - (idx-(n+num)))*2

    else:
        pass

print(idx+1)
