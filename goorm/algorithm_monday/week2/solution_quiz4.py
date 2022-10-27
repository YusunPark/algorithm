# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, k = map(int, input().split())

dys = [0, -1, 1, 0, 0]
dxs = [0, 0, 0, -1, 1]

count = 0

def is_range(y, x):
	return 0 <= y < n and 0 <= x < n

def boom(y, x):
	global count
	
	for dy, dx in zip(dys, dxs):
		if is_range(y+dy, x+dx):
				count += 1

for i in range(k):
	y, x = map(int, input().split())
	boom(y-1, x-1)

print(count)
