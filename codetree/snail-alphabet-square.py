


n, m = map(int, input().split())

grid = [[0] * m for _ in range(n) ]

def is_range(y, x):
    if y < 0 or y >= n or x < 0 or x >= m:
        return False
    
    if grid[y][x] != 0:
        return False

    return True

d = 0
dys = [0, 1, 0, -1]
dxs = [1, 0, -1, 0]
pos_y, pos_x = 0, 0

for i in range(n*m):
    # 다시 A로 초기화 
    i = i % 26
    grid[pos_y][pos_x] = chr(i+65)

    if is_range(pos_y+dys[d], pos_x+dxs[d]):
        pos_y += dys[d]
        pos_x += dxs[d]
    
    else:
        d = (d+1) % 4
        pos_y += dys[d]
        pos_x += dxs[d]

    
for l in grid:
    print(" ".join(map(str, l)))
