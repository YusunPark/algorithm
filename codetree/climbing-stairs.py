# dp (memo)
# 2칸을 가면되는 경우 + 3칸을 가면되는 경우

import sys

n = int(input())
result = [0 for _ in range(n+1)]

def memo(n):


    if n == 2 or n == 3:
        result[n] = 1
    else:
        if n-2 > 1:
            result[n] += result[n-2] 
        if n-3 > 1:
            result[n] += result[n-3]

for i in range(1, n+1):
    memo(i)

print(result[n] % 10007)