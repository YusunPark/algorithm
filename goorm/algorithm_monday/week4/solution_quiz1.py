# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
from collections import deque

n, m = map(int, input().split())
wallet = n
pendding = deque([])

for _ in range(m):
	
	cmd, num = input().split()
	num = int(num)
	
	if cmd == 'deposit': 
		wallet += num
		for _ in range(len(pendding)):
			if pendding[0] <= wallet: 
				wallet -= pendding.popleft()
			else:
				break
				
	elif cmd == 'pay' and num <= wallet :
		wallet -= num
	elif cmd == 'reservation':
		if len(pendding) == 0 and num <= wallet:
			wallet -= num
		else:
			pendding.append(num)
		
	
print(wallet)