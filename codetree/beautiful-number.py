
n = int(input())
arr = []
result = 0

def check(number):
    num = 0
    count = 0
    for i in number:
        if count == 0:
            num = i
            count = i

        if i == num: # 같은 숫자인 경우
            count -= 1
        else:
            return False
    if count != 0:
        return False
    return True

  
def choose(curr_num):
    global result
    if curr_num > n:
        if check(arr):
            result += 1
        return 
    for i in range(1, 5):
        arr.append(i)
        choose(curr_num+1)
        arr.pop()
    


choose(1)
print(result)