# 자신의 뒤의 수보다 크면 1, 아니면 0으로 값을 주어서 stack 탐험을 하지 않도록 구현


from collections import deque


result = []
n = int(input())
height = list(map(int, input().split(" ")))

top = deque()
one_stack = deque()

for i in range(0, n-1):
    if height[i] >= height[i+1]:
        top.append((height[i],i+1, 1))
        one_stack.append((height[i],i+1))  
    else:
        top.append((height[i],i+1, 0))
top.append((height[-1],n, 0))

print(top)
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
            one_value1 = one_stack.pop()
            while array:
                array_value = array.popleft()
                if array_value[0] >= one_value1[0]:
                    array.append(array_value)
                    # result = str(0) + ' ' + result
                else:
                    result[array_value[1]] = one_value1[0]
                    # result = str(one_value1[1]) + ' ' + result
            # print(top)
            # print(one_stack)
            # print(result)
            if len(one_stack) == 0:
                result[value[1]] = 0
                # result = str(0) + ' ' + result
                break
            else:
                one_value2 = one_stack.pop()
                if one_value2[0] < one_value1[0]:
                    result = str(0) + ' ' + result
                else: 
                    result = str(one_value2[1]) + ' ' + result
                one_stack.append(one_value2)
        
        # 자신이 뒤보다 작을 경우
        else:
            # print(top)
            # print(one_stack)
            # print(result)
            array.append(value)


for _ in range(len(top)):
    result = str(0) + ' ' + result

print(result[:-1])

