from itertools import permutations

n,m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

printed = set([])
result = []

for case in permutations(arr, m):
    result.append(case)

for list_ in result:
    if list_ not in printed:
        print(' '.join(map(str, list_)))
        printed.add(list_)
