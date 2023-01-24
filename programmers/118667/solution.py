from collections import deque


def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    result = 0
    count = len(queue1) * 4
    if (sum1+sum2)%2 == 1: 
        return -1

    while(sum1 != sum2 and count > 0):
        if sum1 > sum2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum1 -= tmp
            sum2 += tmp
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum1 += tmp
            sum2 -= tmp
        
        
        count -= 1
        result += 1
        if sum1 == 0 or sum2 == 0:
            return -1

    if sum1 != sum2 :
        return -1
    return result