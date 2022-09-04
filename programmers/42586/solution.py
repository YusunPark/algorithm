import math


def solution(progresses, speeds):
    answer = []
    working_days = [
        math.ceil((100 - p) / s)
        for p, s in zip(progresses, speeds)
    ]
    q = 0
    for i in range(len(working_days)):
        if working_days[i] > working_days[q]:
            answer.append(i - q)
            q = i
    answer.append(len(working_days) - q)
    return answer


print(solution([93, 30, 55], [1, 30, 5]))
