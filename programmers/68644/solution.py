from itertools import combinations


def solution(numbers):
    return sorted(list(set(sum(comb) for comb in combinations(numbers, 2))))


result = solution([2, 1, 3, 4, 1])
print(result)
