def solution(citations):
    citations.sort(reverse=True)
    i = len(citations)
    while(i > 0):
        count = 0
        for val in citations[:i]:
            if val < i:
                i -= 1
                break
            count += 1
        if count == i:
            return count
            
    return 

res = solution([3, 0, 6, 1, 5])
print(res)
