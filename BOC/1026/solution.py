n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
print(sum([x*y for x,y in zip(a,b)]))