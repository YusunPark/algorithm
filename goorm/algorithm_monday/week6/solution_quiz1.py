# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

for _ in range(5):
	num = input()

	a = 0
	for i in range(1, len(num)+1):
		if i % 2 == 1:
			a += int(num[i-1])

	for i in range(1, len(num)+1):
			if i % 2 == 0 and int(num[i-1]) != 0:
				a *= int(num[i-1])


	print(a % 10)