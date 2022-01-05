import numpy as np


def solution(arr1, arr2):
    return (
        np.array(arr1) + np.array(arr2)
    ).tolist()


if __name__ == "__main__":
    arr1 = [
        [[1, 2], [2, 3]],
        [[1], [2]]
    ]
    arr2 = [
        [[3, 4], [5, 6]],
        [[3], [4]]
    ]

    for i, case in enumerate(zip(arr1, arr2), start=1):
        result = solution(*case)
        print(f'{i}번째 테스트: {result}')
