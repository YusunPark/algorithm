n, m = map(int, input().split())
r, c, d = map(int, input().split())

grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

dys = [-1, 0, 1, 0]
dxs = [0, 1, 0, -1]

def is_range(y, x):
    return 0 <= y < n and 0 <= x < m

run = True
clean = 0
while(run):
    # print(r,c,d)
    # 청소 x
    if grid[r][c] == 0: 
        grid[r][c] = 2
        clean += 1

    # 청소 o
    else:
        next_space = False
        for i in range(1, 5):
            temp_d = (d-i)%4
            if is_range(r+dys[temp_d],c+dxs[temp_d]) and grid[r+dys[temp_d]][c+dxs[temp_d]] == 0:
                r, c = r+dys[temp_d] , c+dxs[temp_d]
                d = temp_d
                next_space = True
                break

        if next_space == False:
            # 주변이 없는 경우
            if is_range(r-dys[d],c-dxs[d]):
                if grid[r-dys[d]][c-dxs[d]] == 1:
                    run = False
                elif grid[r-dys[d]][c-dxs[d]] == 2:
                    r, c = r-dys[d],c-dxs[d]
                

print(clean)

