# 아이디어
# : 1행의 숫자값 (input값)을 저장하고 주어진 값과 1행의 값의 차이를 구해서 진행

num = int(input())
sum = 1
i = 1

while(num > sum):
    if num == sum:
        break
    sum += i
    i += 1


if sum != num:
    i -= 1
    sum -= i

dif = num - sum

if i % 2 == 0:
    print(f'{1+dif}/{i-dif}')
else:
    print(f'{i-dif}/{1+dif}')

    
