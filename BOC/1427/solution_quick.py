def quick(array, start, end):
    if start < end:
        pivot = start
        j = pivot+1

        for i in range(start+1, end):
            if array[pivot] < array[i]:
                array[i], array[j] = array[j], array[i]
                j += 1
            else:
                pass
    
        array[start], array[j-1] = array[j-1], array[start]
        quick(array, start, j-1)
        quick(array, j, end)




n = int(input())
num = []

while(1):
    if n//10 == 0:
        num.append(n)
        break
    else:
        num.append(n%10)
        n = n//10
quick(num, 0, len(num))

s = 0
for i in num:
    s = s*10+i
print(s)