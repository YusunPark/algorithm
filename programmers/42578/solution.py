def solution(clothes):
    dict_ = {}
    for x, y in clothes:
        if y in dict_:
            dict_[y] += 1
        else:
            dict_[y] = 1
        
    answer = 1
    for val in dict_.values():
        answer *= val+1
    
    return answer-1

result = solution([
    ["yellow_hat", "headgear"],
    ["blue_sunglasses", "eyewear"],
    ["green_turban", "headgear"]
])

print(result)
