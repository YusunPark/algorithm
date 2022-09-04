def solution(s):
    if len(s)%2 == 0:
        idx = len(s)//2-1
        return s[idx:-idx]
    
    else:
        return s[len(s)//2]


if __name__ == "__main__":
    test_cases = [
        ["abcde"], 
        ["qwer"]
    ]

    for case in test_cases:
        result = solution(*case)
        print(result)
