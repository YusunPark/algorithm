# dfs

def Search(search, start, origin, virus):
    for i in start[origin]:
        if i not in search:
            search.add(i)
            virus = virus + 1
            if i in start:
                virus = Search(search, start, i, virus)
        
        else: pass
    return virus
    


count = int(input())
couple = int(input())
start = {}

for i in range(1, couple+1):
    a,b = map(int, input().split(" "))
    if a in start:
        start[a].append(b)
    else:
        start[a] = [b]

    if b in start:
        start[b].append(a)
    else:
        start[b] = [a]


virus = 0
search = set([1])
virus = Search(search, start, 1, virus)
print(virus)
