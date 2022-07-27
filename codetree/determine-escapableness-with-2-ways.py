# 좌측 상단에서 시작,  (우측, 아래)로만 움직일 수 있다
# 탈출 가능 경로가 있는지 확인하기

dxs = [1, 0]
dys = [0, 1]

n, m = map(int, input().split())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
visited = [[0]*m for _ in range(n)]

stop = False

def is_range(y, x):
    return 0 <= y < n and 0 <= x < m 

def move(y, x):
    global stop

    if y == n-1 and x == m-1:
        stop = True
        return 1

    for dy, dx in zip(dys, dxs):
        if is_range(y+dy , x+dx) and visited[y+dy][x+dx] == 0 and grid[y+dy][x+dx] == 1:
            visited[y+dy][x+dx] = 1
            move(y+dy , x+dx)
  
    if stop: return  1
    else: return 0

print(move(0,0))


