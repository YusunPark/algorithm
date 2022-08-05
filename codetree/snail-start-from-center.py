n = int(input())

pos_y, pos_x = n-1, n-1

d = 0
dys = [0, -1, 0, 1]
dxs = [-1, 0, 1, 0]

grid = [[0] * n for _ in range(n)]

def canGo(y, x):
    if y < 0 or y >= n or x < 0 or x >= n:
        return False
    if grid[y][x] != 0:
        return False
       
    return True


for i in reversed(range(1, n*n+1)):
    grid[pos_y][pos_x] = i

    if canGo(pos_y+dys[d], pos_x+dxs[d]):
        pos_y += dys[d]
        pos_x += dxs[d]
    
    else:
        d = (d+1) % 4
        pos_y += dys[d]
        pos_x += dxs[d]

for l in grid:
    print(" ".join(map(str, l)))