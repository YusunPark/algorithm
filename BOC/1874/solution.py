# 아이디어
# 1. 수열중에서 제일 앞의 값을 타켓으로 선정
# 2. 1부터 n 까지 반복문을 돌면서 stack 에 값을 넣는다. 
# 3. 이 과정에서 stack의 최상단 값과 타겟이 일치하면 둘 다 뺀다.
# 4. 한번 빼고나면 타겟을 바꾸고 다시 3번을 실행한다. (반복)
# 5. (stack에 값이 다 넣어진 경우) 수열 값이 남은 상태에서 종료가 되면 stack 과 비교하여 나머지 처리를 해준다.

from collections import deque

n = int(input())
result = ''

# 주어진 수열을 담을 자료형 queue 생성 후 값 삽입
queue = deque()
for _ in range(n):
    queue.append(int(input()))


# 1부터 n까지 오름차로 값을 임시 저장할 stack 생성
stack = deque()
value = queue.popleft()


for i in range(1, n+1):
    # i보다 수열의 값이 더 클 때 (stack에 값을 넣는다.)
    if value > i:
        result += "+\n"
        stack.append(i)
     

    # 수열의 값과 일치할 때 
    elif value == i:
        # value = i 인 값을 stack에 들어가자마자 바로 나오게 되니까
        result += "+\n"
        result += "-\n"
        

        # 다음 값들을 확인 : stack에 값이 들어있을 경우 반복
        while stack:
            pre_value = queue.popleft()
            pre_stack = stack.pop()

            # 다음 값들도 동일하면, 뺀다. -> 타켓 업데이트 필수
            if pre_value == pre_stack:
                result += "-\n"
                value = pre_value

            # 다르다면, 타겟만 업데이트 해준뒤 break로 나간다.
            else: 
                stack.append(pre_stack)
                value = pre_value
                break
    
        # stack은 0이지만 수열은 남아있는 경우 처리
        # 예시) 수열이 1,2,3,4 인 경우
        if len(stack) == 0 and len(queue) != 0:
            value = queue.popleft()

   
# for 문으로 돌렸기에, 반복문 이후에 남아있는 값이 있을 수 있다.
# 이러한 경우에 처리를 해준다. (위에서처럼, stack/수열 에서 값을 꺼내서 비교)
if len(stack) != len(queue): queue.appendleft(value)
possible = 1

while stack:
    if stack.pop() == queue.popleft():
        result += "-\n"
    else: 
        print("NO")
        possible = 0
        break

if possible: print(result[:-1])
