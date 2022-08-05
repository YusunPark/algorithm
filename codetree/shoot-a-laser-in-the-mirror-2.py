import sys

n = int(input())
mirror = [
    input()
    for _ in range(n)
]

k = int(input())

def is_range(y, x):
    return 0 <= y < n and 0 <= x < n

# 하 좌 상 우 (\)
dys1 = [0, -1, 0, 1]
dxs1 = [1, 0, -1, 0]

# 하 좌 상 우 (/)
dys2 = [0, 1, 0, -1]
dxs2 = [-1, 0, 1, 0]

# 레이저가 들어오는 처음 시작 위치를 정하기 위해서
d = (k-1) // n
if d == 0:
    pos_y = 0
    pos_x = (k-1) % n

elif d == 1:
    pos_y = (k-1) % n
    pos_x = n-1

elif d == 2:
    pos_y =  n-1
    pos_x = n*3 - k 

else:
    pos_y = n*4 - k
    pos_x = 0

count = 0
while(1):
    count += 1

    if mirror[pos_y][pos_x] == '\\': # \
        next_y, next_x = pos_y + dys1[d], pos_x + dxs1[d]
        if is_range(next_y, next_x):
            pos_y, pos_x = next_y, next_x
            
            # 레이저의 방향 바꿈
            if d == 3 or d == 1 :
                d = (d+1)%4
            else:
                d = (d-1)%4
           
        # 격자 밖으로 나간 경우
        else:
            print(count)
            sys.exit()

    else: # /
        next_y, next_x = pos_y + dys2[d], pos_x + dxs2[d]
        if is_range(next_y, next_x):
            pos_y, pos_x = next_y, next_x

            # 레이저의 방향 바꿈
            if d == 0 or d == 2 :
                d = (d+1)%4
            else:
                d = (d-1)%4

        # 격자 밖으로 나간 경우
        else:
            print(count)
            sys.exit()
