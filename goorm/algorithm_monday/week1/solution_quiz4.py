# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import math

n = int(input())
arr = list(map(int, input().split()))
count = arr[1]

def is_prime(n):
	# 1이 아닌 숫자로 나뉘어 지는 가
	for i in range(2, math.ceil(math.sqrt(n))+1):
		if n % i == 0:
			return False	
	return True
		

for i in range(3, n+1):
	if is_prime(i):
		count += arr[i-1]
		
print(count)