count = 0
result = 0

def dfs(arr, idx, target):
    global count
    global result
    if idx == len(arr):
        if count == target:
            result += 1 
        return 
    
    # -
    count -= arr[idx]
    dfs(arr, idx+1, target)
    count += arr[idx]
    # + 
    count += arr[idx]
    dfs(arr, idx+1, target )
    count -= arr[idx]
    
    


def solution(numbers, target):
    global count

    # -
    count -= numbers[0]
    dfs(numbers, 1, target)
    count += numbers[0]
    # +
    count += numbers[0]
    dfs(numbers, 1, target)
    count -= numbers[0]
    
    return result


print(solution([1, 1, 1, 1, 1], 3)) # 5