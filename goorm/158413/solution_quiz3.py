# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n, m = map(int, input().split())

list_ = [
	input().split()
	for _ in range(n)
]

list_.sort()
print(" ".join(list_[m-1]))