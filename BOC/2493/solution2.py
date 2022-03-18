# 자신의 뒤의 수보다 크면 1, 아니면 0으로 값을 주어서 stack 탐험을 하지 않도록 구현


from collections import deque


n = int(input())
height = list(map(int, input().split(" ")))
result = [0]*(n+1)

top = deque()
one_stack = deque()

for i in range(0, n-1):
    if height[i] >= height[i+1]:
        top.append((height[i],i+1, 1))
        one_stack.append((height[i],i+1))  
    else:
        top.append((height[i],i+1, 0))
top.append((height[-1],n, 0))

# print(top)
# print(one_stack)


# 1이면 자동으로 이전꺼 넣고
# 0이면 그 앞을 탐색 한다.
array = deque()
while top:
    value = top.pop()
    if value[1] == 1:
        result[value[1]] = 0

    else:
        # 자신이 뒤보다 클 경우
        if value[2] == 1:
            # print(top)
            # print(one_stack)
            # print(array)
            # print(result)
            one_value1 = one_stack.pop()

            # 뒤에서 0이였던 값이 있었던 경우
            for _ in range(len(array)):
                array_value = array.popleft()
                # 남아있던 값이 1인 값보다 더 큰 경우 -> 계속 남아있다
                if array_value[0] > one_value1[0]:
                    array.append(array_value)
                    
                
                # 남아있던 값이 더 작은 경우 -> 1인 값의 위치
                else:
                    result[array_value[1]] = one_value1[1]

            
            # array와 one_stack이 없는 경우 -> 남은 값 다 0
            if len(one_stack) == 0:
                result[value[1]] = 0
                break
            
            # array는 없고, one_stack은 있는 경우
            else:
                
                one_value2 = one_stack.pop()
                if one_value2[0] < one_value1[0]:
                    result[one_value1[1]] = 0
                    # result = str(0) + ' ' + result
                else: 
                    result[one_value1[1]] = one_value2[1]
                    # result = str(one_value2[1]) + ' ' + result
                
                one_stack.append(one_value2)
            # print(top)
            # print(one_stack)
            # print(array)
            # print(result)

        # 자신이 뒤보다 작을 경우
        else:
            
            array.append(value)
            # print(top)
            # print(one_stack)
            # print(array)
# print(top)
# print(one_stack)
# print(array)
# print(result)

while one_stack:
    one_value = one_stack.pop()
    for _ in range(len(array)):
       value = array.popleft()
       if one_value >= value:
           result[value[1]] = one_value[1]
        
# for _ in range(len(top)):
#     result = str(0) + ' ' + result

a = ''
for x in result[1:]:
    a += str(x) + " "

print(a[:-1])