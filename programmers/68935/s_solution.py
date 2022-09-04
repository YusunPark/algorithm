import numpy as np

def solution(n):
    count = 0
    third = 0
    while n > 2 :
        n, remainder = divmod(n, 3)
        third = third*10+remainder
        count += 1

    third = third*10+n

    count = 0
    answer = 0
    while third > 11:
        third, remainder = divmod(third, 10)
        answer += (3**count)*remainder
        count += 1

    answer += (3**count)*third

    return answer



if __name__ == "__main__":
    test_cases = [
        45, 125
    ]

    for case in test_cases:
        result = solution(case)
        print(result)
