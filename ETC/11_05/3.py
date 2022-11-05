world = []
dys = [0, 1, 1, 1, 0, -1, -1, -1]
dxs = [1, 1, 0, -1, -1, -1, 0, 1]
count = 999999999

def is_range(y, x):
    return 0<= y < len(world) and 0 <= x < len(world)

def can_go(y, x, d):
    if is_range(y+dys[d], x+dxs[d]):
        return world[y+dys[d]][x+dxs[d]] == '.'
    
def check(y, x, d, t):
    global world
    global count

    if y == len(world)-1 and x == len(world)-1:
        if count > t: count = t
        return
    
    
    if world[y][x] == 'X' or t >= count: return    
    
    if is_range(y+dys[d], x+dxs[d]):
        if d % 2 == 1:
            if can_go(y, x, d-1) and can_go(y,x,d+1):
                check(y+dys[d], x+dxs[d], d, t+1)
        else:
            check(y+dys[d], x+dxs[d], d, t+1)

    if is_range(y+dys[d+1], x+dxs[d+1]):
        check(y+dys[d+1], x+dxs[d+1], d+1, t+1)
    
    if is_range(y+dys[d-1], x+dxs[d-1]):
        check(y+dys[d-1], x+dxs[d-1], d-1, t+1)

    return



def solution(worldmap):
    global world
    world = worldmap
    
    direction = 0
    time = 0
    check(0, 0, direction, time)
   
    return count