from functools import reduce


def solution(n):
    return reduce(
        lambda a, b: [
            a[1],
            a[0] + a[1]
        ],
        range(n),
        [0, 1]
    )[1] % 1234567


if __name__ == "__main__":
    for i, case in enumerate([4, 3], start=1):
        result = solution(case)
        print(f'{i}번째 테스트: {result}')
