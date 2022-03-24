from collections import deque

n, w, l = map(int, input().split(" "))

# 트럭의 무게를 저장할 queue
queue = deque()

# 다리위에 올라간 트럭들의 무게 queue와 그 합
weight = deque()
sum_ = 0

# 총 걸린 시간
time = 0


for x in map(int, input().split(" ")):
    queue.append(x)


# 두 queue가 모두 없을 때 까지
while queue or weight:
   
    # 다리 길이만큼만 합산 처리
    if len(weight) == w:
        sum_ -= weight.popleft()
    
    # 모든 트럭이 다리위로 올라간 상태 
    #  -> 마지막 트럭이 걸리는 시간 더해주고 끝내기
    if len(queue) == 0:
        time += w
        break
    
    time += 1
    temp = queue.popleft()
    if sum_ + temp > l:     # 무게 초과시 
        queue.appendleft(temp)
        weight.append(0)    #-> weight에 0을 추가해서 len(weight)가 작동하도록 함
        
    else:
        sum_ += temp
        weight.append(temp)

print(time)