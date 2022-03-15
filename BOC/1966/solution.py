# 자신보다 우선순위가 높은게 있다면 -> 해당 문서를 제일 뒤로

# 1. 총 테스트 횟수
# 2. 문서의 개수 + 궁금한 문서가 어디에 있는지
# 3. n개 문서의 중요도
from queue import Queue


def findMax(array, value):
    for x in array:
        if x > value:
            value = x
        else: pass
    return value

def outQueue(queue, priority, cnt):
    value = queue.get()
    max_value = findMax(priority, value)
    while(1):
        if  value == max_value:
            cnt += 1
            return value, cnt

        else:
            queue.put(value)
            value = queue.get()

result = ''

for _ in range(int(input())):
    cnt = 0
    n, m = map(int, input().split(" "))
    priority = list(map(int, input().split(" ")))
    queue = Queue()

    for i in range(n):
        queue.put(priority[i])

    while(1):
        value, cnt = outQueue(queue, priority, cnt)
        if value == priority[m]:
            result += str(cnt) + '\n'
            break
        else:
            priority.remove(value)

print(result[:-1])

