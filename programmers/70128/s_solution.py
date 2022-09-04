import numpy as np

def solution(a, b):
    a = int(np.dot(a,b))
    return a



if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 4], [-3, -1, 0, 2]),
        ([-1, 0, 1], [1, 0, -1])
    ]

    for case in test_cases:
        result = solution(*case)
        print(result)
