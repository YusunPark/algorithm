# 아이대어
# 거리의 차이를 게산해서 가장 큰 값을 삭제한다. (3개 지점을 통해서 가운데 기준 앞 뒤 거리 +한거랑 1,3 거리 비교)

def calculate_distance(one, two):
    return sum([abs(x - y)  for x, y in zip(one, two)])

n = int(input())
checkpoint = [
    list(map(int, input().split()))
    for _ in range(n)
]

max_value = 0
del_idx = 1
result = 0

for idx in range(1,n-1):
    one = calculate_distance(checkpoint[idx-1], checkpoint[idx])   
    two = calculate_distance(checkpoint[idx], checkpoint[idx+1])   
    jump = calculate_distance(checkpoint[idx-1], checkpoint[idx+1])   

    if max_value < (one+two-jump):
        max_value = (one+two-jump)
        del_idx = idx

del checkpoint[del_idx]

for idx in range(1, n-1):
    result += calculate_distance(checkpoint[idx-1], checkpoint[idx])

print(result)