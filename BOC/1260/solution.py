from collections import deque

n, m, v = map(int, input().split(" "))

dict = {}
for i in range(1, n+1):
    dict[i] = []


for _ in range(m):
    a, b = map(int, input().split(" "))
    dict[a].append(b)
    dict[b].append(a)

# 정렬
for value in dict.values():
    value.sort()

# DFS
def dfs(visited, dict, value):
    if value not in visited:
        visited.append(value)
        for x in dict[value]:
            if x in visited:
                pass
            else: 
                dfs(visited, dict, x)
        return
                

# BFS
def bfs(visited, dict, value, queue ):
    if value not in visited:
        visited.append(value)
    for x in dict[value]:
        if x not in visited:   
            queue.append(x)
            visited.append(x)
    while queue:
        v = queue.popleft()

        for i in dict[v]:
            if i not in visited:
                queue.append(i)
                visited.append(i)
    return
    
        

visited = []
dfs(visited, dict, v)  

result = ''
for i in visited:
    result+= str(i) + ' '
print(result[:-1])

visited = []
queue = deque()
bfs(visited, dict, v, queue)  

result = ''
for i in visited:
    result+= str(i) + ' '
print(result[:-1])