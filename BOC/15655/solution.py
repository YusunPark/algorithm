from itertools import permutations

n, m = map(int, input().split())
array = list(map(int, input().split()))
array.sort()

for case in permutations(array, m):

    if list(case) == sorted(case):
        print(" ".join(map(str, case)))


