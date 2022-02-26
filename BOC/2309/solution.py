height = []
total = 0
stop = False

for i in range(9):
    height.append(int(input()))
    total += height[i]

for i in range(9):
    for j in range(i+1,9):
        if total-height[i]-height[j] == 100:
            a, b = height[i], height[j]
            height.remove(a)
            height.remove(b)
            height.sort()
            stop = True
            break
    if stop == True:
        break

for i in height:
    print(i)
            



    
