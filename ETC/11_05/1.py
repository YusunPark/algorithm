def solution(line):
    prev = ''
    answer = ''
    flag = False
    for v in line:
        if v != prev: 
            if flag:
                answer += '*'
            answer += v
            prev = v
            flag = False
        else:
            flag = True
    if flag:
        answer += '*'    
    return answer