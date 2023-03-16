n = int(input())
a = list(map(int, input().split()))
b, c  = map(int, input().split())

# 총감독관은 모든 시험장에 있어야하기때문에
count = n

for student in a:
    student -= b
    if student > 0:
        count += student // c
        if student % c != 0: count += 1 

print(count)



