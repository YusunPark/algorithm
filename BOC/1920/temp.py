def solution(s):
    numstrDict = {'zero' : '0', 'one' : '1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine': '9'}
    temp = ''
    for i in s:
        temp += i
        if temp in numstrDict:
            print(temp)
            s = s.replace(temp, numstrDict[temp])
    print(s)
    return 

s = input()
solution(s)