def solution(a, b):
    arr = [a, b]
    
    answer = 0
    for i in range(min(arr), max(arr)+1):
        answer += i
    return answer


def solution2(a, b):
    
    return sum(range(min(a,b), max(a,b)+1))



if __name__ == "__main__":
    for case in [[3, 5], [3, 3], [-4, -7], [-3, 1]]:
        result = solution(case[0], case[1])
        result2 = solution2(case[0], case[1])
        print(result)
        print(result2)