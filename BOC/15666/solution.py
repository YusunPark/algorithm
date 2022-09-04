n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr = list(set(arr))
arr.sort()

result = []



def choose(curr_num):
    global m
    if curr_num > m:
        if sorted(result) == result:
            print(" ".join(map(str, result)))
        return 
    
    for i in arr:
        result.append(i)
        choose(curr_num+1)
        result.pop()


choose(1)
    
    

