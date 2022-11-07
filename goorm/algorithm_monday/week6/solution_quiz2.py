# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# chr(97) = a
import math
n = int(input())
secret = input()
result = ''

for i in range(0,n,2):
	pow_num = int(math.pow(int(secret[i+1]),2))
	num = ord(secret[i]) + pow_num
	if num > 122:
		result += chr((num % 123) + 97)
	else:
		result += chr(num)
	
print(result)