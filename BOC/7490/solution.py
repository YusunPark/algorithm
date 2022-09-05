n = int(input())
testcase = [
    int(input())
    for _ in range(n)
]

tool = [ ' ', '+', '-']

arr = []

def check(test_num):
    num_arr = list(range(1, test_num+1))
    new_case = [num_arr[0]]
    new_tool = []

    # ' ' 인 경우 합치는 작업
    for i in range(1, test_num):
        if arr[i-1] == ' ':
            tmp = new_case[-1]*10 + num_arr[i]
            new_case[-1] = tmp
        else:
            new_case.append(num_arr[i])
            new_tool.append(arr[i-1])
    
    # 실제로 계산을 하는
    result = new_case[0]
    for i in range(1, len(new_case)):
        if new_tool[i-1] == '+':
            result += new_case[i]
        else:
            result -= new_case[i]
    if result == 0:
        s = str(num_arr[0])
        for i, v in enumerate(arr):
            s += v + str(num_arr[i+1])

        print(s)
    return 

        
# ' ' +, - 를 고르는 부분
def choose(curr_num, test_num):
    if curr_num == test_num:
        check(test_num)
        return

    for i in tool:
        arr.append(i)
        choose(curr_num+1, test_num)
        arr.pop()



def run(test_num):
    choose(1, test_num)
    print("")

# 여러 테스트 케이스를 분리 하는 부분
for test_num in testcase:
    run(test_num)
