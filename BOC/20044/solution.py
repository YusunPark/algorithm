n = int(input())
score = list(map(int, input().split()))
score.sort()
sum_score = []

for i in range(n):
    # print(i)
    # print(score[i] , score[2*n-1-i])
    sum_score.append(score[i] + score[2*n-1-i])

print(min(sum_score))