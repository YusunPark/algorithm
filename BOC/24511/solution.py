# 자료구조가 stack 인 경우에는 넣은 값이 그대로 나오므로 변화 x
# 자료구조가 Queue 인 경우에는 이전의 값이 나오므로 변화함 -> Queue만 고려

# 처음에 값을 넣고 빠져나온 값으로 다시 QueueStack 을 진행하니까 
# 제일 마지막 Queue의 값이 리턴 값임

from sys import stdin

n = int(stdin.readline())
qs = list(map(int,stdin.readline().split()))
container = list(stdin.readline().split())

m = int(stdin.readline())
c = list(stdin.readline().split(" "))
    
queue = []
for i in range(n):
    # 자료구조가 Queue 인경우 queue 리스트에 넣기
    # [1, 4]
    if qs[i] == 0:
        queue.append(container[i])

# [4, 1]
queue.reverse()
# [4, 1, 2, 4, 7]
queue.extend(c)
print(" ".join(queue[:m]))