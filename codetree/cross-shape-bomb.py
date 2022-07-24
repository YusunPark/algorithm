n = int(input())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

r, c = map(int, input().split())
r, c = r-1, c-1

def is_range(y,x):
    return 0 <= y < n and 0 <= x < n

def shift(grid, y, x):
    if is_range(y,x):
        for i in reversed(range(y)): # y = 2 -> 1, 0
            grid[i+1][x] = grid[i][x]
        grid[0][x] = 0 

value = grid[r][c]

# grid[]
# 행 (세로의 길이 = 2-> 3 3-> 5)
for i in range(2*value-1):
    shift(grid, r-value+1+i, c)

# 열
for i in range(1, value):
    shift(grid, r, c-i)
    shift(grid, r, c+i)

for i in grid:
    print(" ".join(map(str, i)))    
