from sys import stdin
n = int(stdin.readline())
qs = list(map(int,stdin.readline().split()))
container = list(stdin.readline().split())

m = int(stdin.readline())
c = list(stdin.readline().split(" "))
    
queue = []
for i in range(n):
    if qs[i] == 0:
        queue.append(container[i])
queue.reverse()
queue.extend(c)
print(" ".join(queue[:m]))