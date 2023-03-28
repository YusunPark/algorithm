# A 회전 이전 맞닿은 극이 다르면 (SN) -> B는 반대로 회전
#  같으면 -> 회전 x
# 왼쪽 -2 / 오른쪽 2 -> 인덱스를 확인  (i => 각 톱니의 북쪽의 index)
gear = {}
idx = {}
d = [-1, 1]
r = [0, 0, 0, 0]

for i in range(1, 5):
    gear[i] = list(input())
    idx[i] = 0

k = int(input())


def rotate(num, direc):
    r[num-1] = 1
    # print(r, num, direc)

    # 돌릴 기어 확인
    if 1 < num < 4:
        if r[num-2] == 0 and gear[num][(idx[num]-2)%8] != gear[num-1][(idx[num-1]+2)%8]:
            rotate(num-1, (direc+1) % 2)

        if r[num] == 0 and gear[num][(idx[num]+2)%8] != gear[num+1][(idx[num+1]-2)%8]:
            rotate(num+1, (direc+1) % 2)

    elif num == 1:
        if r[num] == 0 and gear[num][(idx[num]+2)%8] != gear[num+1][(idx[num+1]-2)%8]:
            rotate(num+1, (direc+1) % 2)

    elif num == 4:
        if r[num-2] == 0 and gear[num][(idx[num]-2)%8] != gear[num-1][(idx[num-1]+2)%8]:
            rotate(num-1, (direc+1) % 2)
    else:
        return

    # 기어 돌리기
    idx[num] = (idx[num] - d[direc]) % 8


for _ in range(k):
    # 회전 유무 초기화
    r = [0, 0, 0, 0]
    number, direc = map(int, input().split())
    # print(number, direc)
    if direc == -1:
        rotate(number, 0)
    else:
        rotate(number, 1)

    # print(idx)

result = 0

for i, v in enumerate(idx.values()):
    # print(gear[i+1])
    if gear[i+1][v] == '1':
        result += 2**i

print(result)
