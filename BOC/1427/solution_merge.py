import math


def merging(array, s1, e1, s2, e2):
    result = []
    p = s1
    q = s2

    while(1):
        if p > e1:
            result.extend(array[q:e2+1])
            break
        elif q > e2:
            result.extend(array[p:e1+1])
            break
        else:
            if array[p] > array[q]:
                result.append(array[p])
                p += 1
            else:
                result.append(array[q])
                q += 1

    array[s1:e2+1] = result



def divide(array, start, end):
    if start == end:
        return 

    else:
        middle = math.floor((start+end)/2)
        divide(array, start, middle)
        divide(array, middle+1, end)
        merging(array, start, middle, middle+1, end)



n = int(input())
num = []

while(1):
    if n//10 == 0:
        num.append(n)
        break
    else:
        num.append(n%10)
        n = n//10

divide(num, 0, len(num)-1)


s = 0
for i in num:
    s = s*10+i

print(s)
