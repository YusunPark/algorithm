h, w, x, y = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(h+x)
]

for i in range(h):
    for j in range(w):
        grid[x+i][y+j] -= grid[i][j]

for i in range(h):
    print(" ".join(map(str, grid[i][:w])))