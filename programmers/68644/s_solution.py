def solution(numbers):
    answer = []
    
    for x in range(len(numbers)):
        for y in range(len(numbers)):
            if(x != y):
                sum = numbers[x]+numbers[y]
                if sum not in answer:
                    answer.append(sum)
    answer.sort()    
    return answer

result = solution([2, 1, 3, 4, 1])
print(result)
