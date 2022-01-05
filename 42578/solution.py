from collections import Counter
from functools import reduce


def solution(clothes):
    return reduce(
        lambda x,y : x * (y + 1),
        Counter(x for _, x in clothes).values(), 1
    ) - 1


result = solution([
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"]
])


print(result)
