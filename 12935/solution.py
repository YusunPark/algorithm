def solution(arr):
    arr.remove(min(arr))
    return arr or [-1]

if __name__ == '__main__':
    test_cases = [
        [4, 3, 2, 1],
        [10]
    ]

    for test_case in test_cases:
        print(solution(test_case))
