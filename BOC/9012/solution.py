from unittest import result


n = int(input())
result = []

for i in range(n):
    ps = input()
    sum = 0
    for x in ps:
        if x == '(':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            sum = -99999
    if sum == 0:
        result.append('YES')
    else:
        result.append('NO')

for i in result:
    print(i)
