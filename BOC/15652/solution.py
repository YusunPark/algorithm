n,m = map(int, input().split(" "))

array = [x for x in range(1, n+1)]

for i in range(m-1):
    array.extend(array)
print(array)


for i in array:
    print(i)


n,m = map(int, input().split())
 
s = []
 
def dfs(start):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return
    
    for i in range(start, n+1):
        s.append(i)
        dfs(i)
        s.pop()
    
dfs(1)