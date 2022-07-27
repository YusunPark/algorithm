k, n = map(int, input().split())
arr = []

def choose(curr_num):

    if curr_num == n + 1:
        print(" ".join(map(str,arr)))
        return 
    
    # 배열에 값 추가
    for i in range(1, k+1):
        arr.append(i)
        choose(curr_num+1)
        arr.pop()

choose(1)