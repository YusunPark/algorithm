# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

n = int(input())
num = list(map(int, input().split()))
count = 1

for x in num:
	count *= x
	
print(count)
	