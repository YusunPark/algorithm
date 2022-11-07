# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from itertools import cycle

n = int(input())

for _ in range(n):
	s = input()
	cmd, key = input().split()
	result = ''
	
	if cmd == 'E':
		for x, y in zip(s,cycle(key)):
			int_x = ord(x)
			value = ord(x)+(ord(y)%26)
			if 65 <= int_x <= 90:
				result += chr((value-65)%26 + 65)
			elif 97 <= int_x <= 122:
				result += chr((value-97)%26 + 97)
			else:
				result += x
	else:
		for x, y in zip(s,cycle(key)):
			int_x = ord(x)
			value = ord(x)-(ord(y)%26)
			if 65 <= int_x <= 90:
				result += chr((value-65)%26 + 65)
			elif 97 <= int_x <= 122:
				result += chr((value-97)%26 + 97)
			else:
				result += x

	print(result)
	
	