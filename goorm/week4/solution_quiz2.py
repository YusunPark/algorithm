# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
tree = []
for _ in range(n):
	tree.append(list(map(int, input().split())))


# 상 하 좌 우
dys = [-1, 1, 0, 0]
dxs = [0, 0, -1, 1]

day = 0
def is_range(y, x):
	if 0 <= y < n and 0 <= x < n : return True
	return False

flag = True
while(flag):
	value = [[0]*n for _ in range(n)]
	day+=1
	for y in range(n):
		for x in range(n):
			if tree[y][x] != 0:
				count = 0
				for dy, dx in zip(dys, dxs):
					if is_range(y+dy, x+dx) and tree[y+dy][x+dx] == 0: count += 1
				value[y][x] = count

	flag = False
	for y in range(n):
		for x in range(n):
			if value[y][x]:				
				flag = True
				tree[y][x] -= value[y][x] 
				if tree[y][x] < 0 : tree[y][x] = 0

print(day-1)
		
		