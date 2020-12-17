def solution(a, b):
    return sum([x * y for x, y in zip(a, b)])


result = solution(
    [1, 2, 3, 4],
    [-3, -1, 0, 2]
)
