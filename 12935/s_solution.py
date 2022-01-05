def solution(arr):
    if len(arr) == 1:
        return [-1]
    arr.remove(min(arr))
    return arr


if __name__ == "__main__":
    test_cases = [
        ([1])
    ]

    for case in test_cases:
        result = solution(case)
        print(result)
