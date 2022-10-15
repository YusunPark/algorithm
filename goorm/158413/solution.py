# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

for _ in range(int(input())):
	person_num = int(input())
	result = list(map(int, input().split()))
	avg_result = sum(result) / person_num
	count = [1 if i >= avg_result else 0 for i in result]
	print(f'{count.count(1)}/{person_num}')




