import sys

board = [
    list(map(int, input().split()))
    for _ in range(19)
]

def is_range(y, x):
    return 0 <= x < 19 and 0 <= y < 19

def check_right(y, x, value):
    if is_range(y, x+4) and min(board[y][x:x+5]) == max(board[y][x:x+5]) == value:
        if is_range(y, x+5) and board[y][x+5] == value: return False
        elif is_range(y, x-1) and board[y][x-1] == value: return False
        return True
    return False

def check_down(y, x, value):
    if is_range(y+4, x):
        tmp = []
        for i in range(5):
            tmp.append(board[y+i][x])
        if min(tmp) == max(tmp) == value:
            if is_range(y+5, x) and board[y+5][x] == value: return False
            elif is_range(y-1,x) and board[y-1][x] == value: return False
            return True
    return False

def check_r_diagonal(y, x, value):
    if is_range(y+4, x+4):
        tmp = []
        for i in range(5):
            tmp.append(board[y+i][x+i])
        if min(tmp) == max(tmp) == value:
            if is_range(y+5, x+5) and board[y+5][x+5] == value: return False
            elif is_range(y-1,x-1) and board[y-1][x-1] == value: return False
            return True
    return False

def check_l_diagonal(y, x, value):
    if is_range(y+4, x-4):
        tmp = []
        for i in range(5):
            tmp.append(board[y+i][x-i])
        if min(tmp) == max(tmp) == value:
            if is_range(y+5, x-5) and board[y+5][x-5] == value: return False
            elif is_range(y-1,x+1) and board[y-1][x+1] == value: return False
            return True
    return False


for y in range(19):
    for x in range(19):
        if board[y][x] != 0:
            # print(f"시작 {y} {x}")
            if check_right(y, x, board[y][x]) or check_r_diagonal(y, x, board[y][x]) or check_down(y, x, board[y][x]):
                print(board[y][x])
                print(y+1, x+1)
                sys.exit()
            elif check_l_diagonal(y, x, board[y][x]):
                print(board[y][x])
                print(y+5, x-3)
                sys.exit()

print(0)
            
