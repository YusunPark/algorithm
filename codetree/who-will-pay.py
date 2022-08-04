import sys

n, m, k = map(int, input().split())

student = [0]*n

for v in range(m):
    s_id = int(input())
    student[s_id-1] += 1

    if student[s_id-1] == k:
        print(s_id)
        sys.exit()

print(-1)