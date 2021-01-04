from itertools import cycle

def solution(n):

    str = ["수", "박"]
    strCycle = cycle(str)
    answer = ""
    for idx in range(n):
        answer += next(strCycle)
    return answer

def solution2(n):
    return "수박"*(n//2) + "수"*(n%2)
    
n = 7
print(solution(n))
print(solution2(n))