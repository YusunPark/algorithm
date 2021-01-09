def solution(citations):
    citations.sort()
    papers = len(citations)
    for i in range(papers):
        if citations[i] >= papers - i:
            return papers - i
    return 0


res = solution([3, 0, 6, 1, 5])
print(res)
