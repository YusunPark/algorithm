n = int(input())

count = 0
candidate = [] # 선택된 위치를 저장

def is_promising(num):
    length = len(candidate)
    for idx, cand in enumerate(candidate):
        if num == cand or abs(num - cand) == abs(length-idx):
            return False
    return True        

def search(curr_num):
    global count
    if curr_num == n:
        count += 1
        return 
    
    for num in range(n):
        if num not in candidate:
            if is_promising(num):
                candidate.append(num)
                search(curr_num+1)
                candidate.pop()
      
search(0) 
print(count)
            