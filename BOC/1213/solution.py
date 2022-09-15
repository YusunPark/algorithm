# 1. 홀수개 문자열이 1개를 초과하여 존재할 수 없다.
# 2. 사전 순으로 출력되어야 하기 때문에 홀수임에도 3,5,7,등의 개수라면 나머지는 앞에 찍는다.
import sys

str = input()
str = sorted(str)

value, count = "", 0
result = ''
odd_str, odd_count = "", 0

def check():
    global result, count, value, odd_str, odd_count
    if count % 2 == 1: # 문자의 개수가 홀수인게 2개이상이면 불가
        odd_str = value
        odd_count += 1
        if count // 2 > 0: # 3,5,7, 등인 경우
            result += (value*(count//2))

        if odd_count > 1:
            print("I'm Sorry Hansoo")
            sys.exit()
    else:
        result += (value*(count//2))



for s in str:
    # print(s, value)
    if value != s:  # 새로운 문자 발견 
        check()
        
        value = s
        count = 1

    else: # 이전에 나온 문자인 경우 
        count += 1
check()
print(result+odd_str+result[::-1])