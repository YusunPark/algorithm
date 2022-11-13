n = int(input())
room = []
row = 0
col = 0

for _ in range(n):
  tmp = input()
  room.append(tmp)
  
  
  
for y in range(n):
  count = 0
  for x in range(n):
    if room[y][x] == '.':
      count += 1
      if count == 2: 
        row += 1
    else:
      count = 0
  
for x in range(n):
  count = 0
  for y in range(n):
    if room[y][x] == '.':
      count += 1
      if count == 2: 
        col += 1
    else:
      count = 0

print(row, col)


