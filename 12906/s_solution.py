def solution(arr):
    answer = []
    
    for idx, element in enumerate(arr):
        if element == arr[idx-1]:
            if idx == 0:
                answer.append(element)
            else:
                pass
        else:
            answer.append(element)
    
    return answer

def solution2(arr):
    answer = []
    
    for i in arr:
        if answer[-1:] == [i]: continue
        answer.append(i)

    return answer


    
if __name__ == "__main__":
    test_cases = [
        ([1,1,3,3,0,1,1]),
        ([4,4,4,3,3])
    ]
    
    for case in test_cases:
        result = solution(case)
        result2 = solution2(case)
        print(result)
        print(result2)
