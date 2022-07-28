# 방문한 칸들을 적어두고, 그 개수를 출력하면 될 듯?
from collections import deque

n, k = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

pos = [
    list(map(int, input().split()))
    for _ in range(k)
]

visited = [[0]*n for _ in range(n)]

dys = [0, 0, 1, -1]
dxs = [1, -1, 0, 0]


def is_range(y, x):
    if not (0 <= y < n and 0 <= x < n):
        return False
    
    elif visited[y][x] == 1 or grid[y][x] == 1:
        return False
    
    return True


queue = deque()

for p in pos:
    y, x = p
    y, x = y-1, x-1
    visited[y][x] = 1
    queue.append([y, x])
    

count = k

while(queue):
    y, x = queue.popleft()
    
    for dy, dx in zip(dys, dxs):
        if is_range(y+dy, x+dx):
            visited[y+dy][x+dx] = 1
            count +=1
            queue.append([y+dy, x+dx])


# print(visited)
print(count)