import sys

n = int(input())
arr = list(map(int, input().split()))
cmds = list(map(int, input().split())) # + - * /

max_ = -sys.maxsize
min_ = sys.maxsize

def choose(num, curr_num):
  global max_
  global min_
  global n

  if curr_num == n: 
    if num > max_ : max_ = num
    if num < min_ : min_ = num
    return 

  if cmds[0] > 0 : 
    cmds[0] -= 1
    choose(num+arr[curr_num] ,curr_num + 1)
    cmds[0] += 1

  if cmds[1] > 0 : 
    cmds[1] -= 1
    choose(num-arr[curr_num] ,curr_num + 1)
    cmds[1] += 1

  if cmds[2] > 0 : 
    cmds[2] -= 1
    choose(num*arr[curr_num] ,curr_num + 1)
    cmds[2] += 1

  if cmds[3] > 0 : 
    cmds[3] -= 1
    # if num < 0:
    #   print(num, arr[curr_num], num//arr[curr_num],-(abs(num)//arr[curr_num] ))
    #   print(num//arr[curr_num] if num > 0 else -(abs(num)//arr[curr_num] ))
    choose(num//arr[curr_num] if num > 0 else -(abs(num)//arr[curr_num] ) ,curr_num + 1)
    cmds[3] += 1


choose(arr[0], 1)

print(max_)
print(min_)
