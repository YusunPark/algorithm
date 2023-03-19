from collections import deque

n, m = map(int, input().split())

grid = [ input() for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
step = [[0 for _ in range(m)] for _ in range(n)]

dys = [0, 0, 1, -1]
dxs = [1, -1, 0, 0]

q = deque([(0,0)])
step[0][0] = 1

def is_range(y, x):
    return 0 <= y < n and 0 <= x < m

def can_go(y, x):
    return is_range(y, x) and visited[y][x] == False and grid[y][x] == '1'

while q:
    y, x = q.popleft()
    # print(y, x)
    for dy, dx in zip(dys, dxs):
        if can_go(y+dy, x+dx):
            # print("Asda")
            q.append((y+dy, x+dx))
            visited[y+dy][x+dx] = True
            step[y+dy][x+dx] = step[y][x] + 1

# for s in step:
#     print(" ".join(map(str, s)))

print(step[n-1][m-1])


