def solution(a, b):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    d_day = sum(month[:a-1])+b 
    return day[d_day % 7]


if __name__ == "__main__":
    test_cases = [
        [5, 24]
    ]

    for case in test_cases:
        result = solution(*case)
        print(result)
