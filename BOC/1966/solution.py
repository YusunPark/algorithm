from queue import Queue

# 결과를 저장할 result 추가
result = ''

# 매 입력이 들어올 때마다 for문을 실행 (테스트 케이스의 갯수)
for _ in range(int(input())):

    # 입력
    n, m = map(int, input().split(" "))
    priority = list(map(int, input().split(" ")))

    # 큐 : 삽입 삭제가 o(1)
    # priority에 입력한 값들을 큐에 집어넣는 작업 
    # : 이때 인덱스도 저장해서 동일 값이 여러개 있을 경우 구분하는 것으로 사용한다.
    # (priority를 이용하지 않고 바로 큐에 넣는 방법을 모르겠습니다..)
    queue = Queue()
    for i in range(n):
        queue.put((priority[i], i))

    # 최대값 찾는 과정을 빠르게 하기 위한 작업 (정렬을 이용)
    sort_priority = priority.copy()
    sort_priority.sort(reverse=True)

    # 몇번째 출력인지 저장할 변수
    cnt = 0 

    # sort_priority 에서 사용할 인덱스를 따로 만들어줌 (반복문을 덜 쓰기 위해서)
    max_index = 0

    # 실제로 작업을 하는 구간
    while(1):
        max_value = sort_priority[max_index]
        value, index = queue.get()

        # 최대값과 현재 queue에서 나온 값이 같지만 인덱스가 다름 : 빠진걸 다시 넣음
        # 최대값과 현재 queue에서 나온 값이 같고, 인덱스도 같음 : break로 반복문 탈출 및 다음 테스트케이스 실행
        if value == max_value :
            if index != m:
                cnt += 1
                max_index += 1
                queue.put((value, index))
            else: 
                cnt += 1
                result += str(cnt) + '\n'
                break
        else:
            queue.put((value, index))

# 결과 값 출력 (마지막에 \n 이 하나 있어서 슬라이싱 진행)
print(result[:-1])