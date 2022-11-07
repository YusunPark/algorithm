# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
# chr(97) = a
n = int(input())
secret = input()
result = ''

for i in range(0,n,2):
	pow_num = int(secret[i+1])**2
	num = ord(secret[i]) + pow_num
	result += chr(((num-97) % 26) + 97 )
	
print(result)