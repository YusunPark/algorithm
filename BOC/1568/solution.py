n = int(input())
count = 0

while(n):
    for i in range(1, n+1):
        if i > n:
            break
        else: 
            n -= i
            count += 1


print(count)