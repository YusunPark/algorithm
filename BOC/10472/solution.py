from itertools import combinations 

dxs = [0, 0, 0, 1, -1]
dys = [0, 1, -1, 0, 0]

def is_range(y, x):
    return  0 <= y < 3 and 0 <= x < 3

def change_color(y, x):
    for dy, dx in zip(dys, dxs):
        if is_range(dy+y, dx+x):
            if grid[dy+y][dx+x] == "*": grid[dy+y][dx+x] = "."
            else: grid[dy+y][dx+x] = "*"

def num2idx(num):
    return num//3, num%3

def search():
    count = 0
    arr = [i for i in range(9)]
    for cnt in range(1, 10):
        for num_list in combinations(arr,cnt):
            for num in num_list:
                y, x = num2idx(num)
                change_color(y,x)
                count += 1
                if goal == grid :
                    print(count)
                    return 

            for num in reversed(num_list):
                y, x = num2idx(num)
                change_color(y,x) # re-change
                count -= 1
    print(0)
    return 

for _ in range(int(input())):
    grid = [["." for _ in range(3) ] for _ in range(3)]
    goal = [
        list(input())
        for _ in range(3)
        ]
    search()
