n, m = map(int, input().split())

# 함수에 인자로 주어진 값에 연결이 되어있는 것을 발견하고 다시 함수의 인자로 넣는다.
# 방문 체크를 set으로 확인하자
arr = {}

visited = set([])

def linkNode(node):
    if node in visited:
        return 
    visited.add(node)
    if node in arr:
        for v in arr[node]:
            linkNode(v)



for _ in range(m):
    start, end = map(int, input().split())

    if start in arr:
        arr[start].append(end)
    else:
        arr[start] = [end]
    if end in arr:
        arr[end].append(start)
    else:
        arr[end] = [start]

linkNode(1)

print(len(visited)-1)