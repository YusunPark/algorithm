# 제일 최소의 값을 구할 땐 heap을 사용한다.

import heapq

n = int(input())
num = list(map(int, input().split()))

pq = []

for i in num:
    heapq.heappush(pq, i)


result = 0
while(len(pq) > 1):
    a = heapq.heappop(pq)
    b = heapq.heappop(pq)
    result += (a+b)
    heapq.heappush(pq, a+b)
    
print(result)

