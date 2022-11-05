def solution(n, student, point):
    value = {}
    win = set([])
    count = 0
    for i in range (1,n+1):
        value[i] = 0
    for i in range(1, int(n/2)+1):
        win.add(i)

    for stuID, p in zip(student, point):
        if stuID in win:
            value[stuID] += p
        else:
            value[stuID] += p
            tmp = set([x for x,y in sorted(value.items(), key = lambda x:(-x[1], x[0]))[:int(n/2)]])
            if len(tmp & win) != n/2:
                win = tmp
                count += 1

    return count 