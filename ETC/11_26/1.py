def solution(flowers):
    answer = set([])
    for start, end in flowers:
        answer.update(list(range(start, end)))
    return len(answer)