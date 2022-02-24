n = int(input())
m = input()
prime = []
count = 0

for i in range(n):
    a = int(m.split(" ")[i])

    if a == 1 : 
        count += 1
        pass
    else :
        for x in range(2, a):
            if a % x == 0:
                count += 1
                break

print(n-count)