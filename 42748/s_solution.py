def solution(array, commands):
    answer = []
    for idx, cmd in enumerate(commands):
        arr = array[cmd[0]-1:cmd[1]]
        arr.sort()

        answer.append(arr[cmd[2]-1])
   
    return answer


if __name__ == "__main__":
    test_cases = [
        ([1, 5, 2, 6, 3, 7, 4] , [[2, 5, 3], [4, 4, 1], [1, 7, 3]])
    ]
    
    for case in test_cases:
        result = solution(*case)
        print(result)
