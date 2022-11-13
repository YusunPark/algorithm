# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())
result = ''
for i in range(1, n+1):
	arr = [' '*(n-i)]
	arr += ['*'*i]
	result += ''.join(arr)
	result +='\n'
	
for i in range(1, n):
	arr = [' '*i]
	arr += ['*'*(n-i)]
	result += ''.join(arr)
	result +='\n'
print(result)