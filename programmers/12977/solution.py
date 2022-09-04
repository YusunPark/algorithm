from itertools import combinations

def solution(nums):
    count = 0
    for comb in combinations(nums, 3):
        num = sum(comb)
        if num < 2:
            continue
        for i in range(2, int(num ** .5) + 1):
            if num % i == 0:
                break
        else:
            count += 1

    return count


solution([1, 2, 7, 6, 4])
