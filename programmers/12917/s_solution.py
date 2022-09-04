def solution(s):
    answer = ''
    for i in range(122, 64, -1):
        if chr(i) in s:
            count = s.count(chr(i))
            answer += chr(i)*count
    return answer


def solution2(s):
    return  ''.join(sorted(s, reverse=True))


    
if __name__ == "__main__":
    test_cases = [
        ("Zbcdefg")
    ]
    
    for case in test_cases:
        result = solution(case)
        result2 = solution2(case)
        print(result)
        print(result2)
