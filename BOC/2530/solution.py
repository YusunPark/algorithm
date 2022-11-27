time = list(map(int, input().split()))
term = int(input())

for i in reversed(range(len(time))):
    if i != 0:
        time[i] += (term%60)
        term = term // 60

        if time[i] >= 60:
            time[i-1] += 1
            time[i] -= 60
    else:
        time[i] += (term%24)
        if time[i] >= 24:
            time[i] -= 24
            
print(" ".join(map(str, time)))
