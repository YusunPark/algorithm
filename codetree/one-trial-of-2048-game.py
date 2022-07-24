# 1. 사이에 0이 존재하면 뒤로 빼두자
# 근데 90도 회전해서 풀 수 있다고 함,,,

grid = [
    list(map(int, input().split()))
    for _ in range(4)
]
d_str = input()

n = 4

direct = {'L':0, 'R':1, 'U':2, 'D':3}

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def is_range(y, x):
    return 0 <= y < 4 and 0 <= x < 4

def moveZero(grid, d):
    for i in range(n):
        for j in range(n):
            # 좌
            if d == 0 and grid[i][n-1-j] == 0:
                for idx in range(j):
                    grid[i][n-1-(j-idx)] = grid[i][n-1-(j-(idx+1))]
                grid[i][n-1] = 0
            
            # 우
            if d == 1 and grid[i][j] == 0:
                for idx in range(j):
                    grid[i][j-idx] = grid[i][j-(idx+1)]
                grid[i][0] = 0

            # 위
            if d == 2 and grid[n-1-j][i] == 0:
                for idx in range(j):
                    grid[n-1-(j-idx)][i] = grid[n-1-(j-(idx+1))][i]
                grid[n-1][i] = 0

            # 아래
            if d == 3 and grid[j][i] == 0:
                for idx in range(j):
                    grid[j-idx][i] = grid[j-(idx+1)][i]
                grid[0][i] = 0

def sumSame(grid, d):
    
    for i in range(n):
        for j in range(n-1):
     
            # 좌
            if d == 0 and grid[i][j] == grid[i][j+1]:
                grid[i][j] *= 2
                grid[i][j+1] = 0

            # 우
            if d == 1 and grid[i][n-j-1] == grid[i][n-j-2]:
                grid[i][n-j-1] *= 2
                grid[i][n-j-2] = 0
            
            # 위
            if d == 2 and grid[j][i] == grid[j+1][i] :
                grid[j][i] *= 2
                grid[j+1][i] = 0

            # 아래
            if d == 3 and grid[n-j-1][i] == grid[n-j-2][i]:
                grid[n-j-1][i] *= 2
                grid[n-j-2][i] = 0


def __init__ () :
    d = direct[d_str]

    moveZero(grid, d)
    sumSame(grid, d)
    moveZero(grid, d)

    for x in grid:
        print(" ".join(map(str, x)))

__init__()      