# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n, s = input().split()
count = 0
for i in range(int(n)):
	name = input()
	if s in name:
		count += 1
print(count)