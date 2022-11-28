n = int(input())
grid = []

for _ in range(n):
  grid.append(list(input()))

while(len(grid) != 1):
  new_grid = []
  for y in range(0, len(grid), 2):
    tmp = []
    for x in range(0, len(grid), 2):
      if (grid[y][x] == '1') or (grid[y][x] == '0'):
        if grid[y][x] == grid[y][x+1] == grid[y+1][x] == grid[y+1][x+1]:
          tmp.append(grid[y][x])
        else:
          tmp.append(f'({grid[y][x]}{grid[y][x+1]}{grid[y+1][x]}{grid[y+1][x+1]})')

      else: 
        tmp.append(f'({grid[y][x]}{grid[y][x+1]}{grid[y+1][x]}{grid[y+1][x+1]})')
    new_grid.append(tmp)
  grid = new_grid
    
print(grid[0][0])
