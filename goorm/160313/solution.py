a,b = map(int, input().split())
print(abs(a-b)-1 if abs(a-b) != 0 else 0)
arr = [i for i in range(min(a,b)+1, max(a,b))]
print(' '.join(map(str, arr)))

