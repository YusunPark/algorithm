x, y, w, s = map(int, input().split())

if 2*w > s: # 대각선이 직선2번보다 빠를 경우
    if w > s : # 그중에서 대각선 1번이 직선 1회보다 빠를 경우
        if abs(x-y) % 2 == 0:
            print(min(x,y)*s + abs(x-y)*s)
        else:
            print(min(x,y)*s + (abs(x-y)-1)*s + w) 
    else:
        print(min(x,y)*s + abs(x-y)*w)
    
else:# 가로 + 세로 움직이는게 대각선보다 빠를 경우
    print((x+y)*w)
