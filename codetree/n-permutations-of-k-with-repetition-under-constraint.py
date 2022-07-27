k, n = map(int, input().split())
arr = []

def choose(curr_num):
    if curr_num == n + 1:
        print(" ".join(map(str, arr)))
        return 
    
    for i in range(1, k+1):
        if curr_num > 2:
            if arr[curr_num-3] == arr[curr_num-2] == i:
                continue
            
        arr.append(i)
        choose(curr_num + 1)
        arr.pop()

choose(1)