# bfs

from collections import deque

def Search(visited, dict, origin):
    virus = 0
    queue = deque()
    for i in dict[origin]:
        if i not in visited:
            queue.append(i)
    while queue:
        v = queue.popleft()
        if v not in visited:
            visited.add(v)
            queue.extend(dict[v])
            virus = virus + 1
 
        else: pass
    return virus
    


count = int(input())
couple = int(input())
dict = {}

for i in range(1, couple+1):
    a,b = map(int, input().split(" "))
    if a in dict:
        dict[a].append(b)
    else:
        dict[a] = [b]

    if b in dict:
        dict[b].append(a)
    else:
        dict[b] = [a]


virus = 0
visited = set([1])
virus = Search(visited, dict, 1)
print(virus)
