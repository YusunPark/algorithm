import sys

board = [
    list(map(int, input().split()))
    for _ in range(19)
]

def check_right(y, x, value):
    if x+4 < 19 and min(board[y][x:x+5]) == max(board[y][x:x+5]) == value:
        if x+5 < 19 and board[y][x+5] == value: return False
        elif x-1 >= 0 and board[y][x-1] == value: return False
        return True
    return False

def check_down(y, x, value):
    if y+4 < 19:
        tmp = []
        for i in range(5):
            tmp.append(board[y+i][x])
        if min(tmp) == max(tmp) == value:
            if y+5 < 19 and board[y+5][x] == value: return False
            elif y-1 >= 0 and board[y-1][x] == value: return False
            return True
    return False

def check_r_diagonal(y, x, value):
    if x+4 < 19 and y+4 < 19:
        tmp = []
        for i in range(5):
            tmp.append(board[y+i][x+i])
        if min(tmp) == max(tmp) == value:
            if x+5 < 19 and y+5 < 19 and board[y+5][x+5] == value: return False
            elif x-1 >= 0 and y-1 >= 0 and board[y-1][x-1] == value: return False
            return True
    return False

def check_l_diagonal(y, x, value):
    if x-4 >= 0 and y+4 < 19:
        tmp = []
        for i in range(5):
            tmp.append(board[y+i][x-i])
        if min(tmp) == max(tmp) == value:
            if x-5 >= 0 and y+5 < 19 and board[y+5][x-5] == value: return False
            elif x+1 < 19 and y-1 >= 0 and board[y-1][x+1] == value: return False
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
            
