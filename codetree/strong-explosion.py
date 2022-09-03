# 터져야 하는 위치의 정보를 리스트로 관리를 한 다음에
# 개수를 세고 최근 4개의 값을 삭제하면 완벽하게 pop을 할 수 있다.

bomb_x1 = [0, 0, 0, 0, 0]
bomb_y1 = [0, -1, -2, 1, 2]

bomb_x2 = [0, 0, 0, -1, 1]
bomb_y2 = [0, -1, 1, 0, 0]

bomb_x3 = [0, -1, -1, 1, 1]
bomb_y3 = [0, -1, 1, -1, 1]

n = int(input())
grid = [list(map(int, input().split(" "))) for _ in range(n)] # 런타임 에러
# grid = [list(map(int, input().split())) for _ in range(n)] # 정상 작동

pos_one = []
pos_bomb = []
max_count = 0

# 3. 실제 폭탄이 터질 위치 계산 + 개수 파악
def check(pos_bomb):
    tmp_pos = set(pos_bomb)
    pos = []
    for y, x in tmp_pos:
        if 0 <= x < n and 0 <= y < n:
            pos.append([y, x])
    
    return len(pos)
        

# 2. 폭탄의 종류에 따라 영향이 미치는 범위 파악
def choose(curr_num):
    global pos_bomb
    global max_count
   
    if curr_num == len(pos_one):
        count = check(pos_bomb)
        if max_count < count:
            max_count = count
        return 

    y = pos_one[curr_num][0]
    x = pos_one[curr_num][1]

    for dy, dx in zip(bomb_y1, bomb_x1): 
        pos_bomb.append((y+dy, x+dx))
    choose(curr_num+1)
    pos_bomb = pos_bomb[:-5]

    
    for dy, dx in zip(bomb_y2, bomb_x2): 
        pos_bomb.append((y+dy, x+dx))
    choose(curr_num+1)
    pos_bomb = pos_bomb[:-5]

    for dy, dx in zip(bomb_y3, bomb_x3): 
        pos_bomb.append((y+dy, x+dx))
    choose(curr_num+1)
    pos_bomb = pos_bomb[:-5]


# 1. 폭탄이 터질 위치를 파악하기 위한 함수
def find_one():
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                pos_one.append([i, j])




find_one()
choose(0)
print(max_count)



