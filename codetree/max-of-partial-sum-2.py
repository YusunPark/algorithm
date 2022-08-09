import sys

n = int(input())
arr = list(map(int, input().split()))

maxValue, sumValue = -sys.maxsize , 0
start, end = 0, 0

for i, v in enumerate(arr):
    sumValue += v

    if sumValue < 0 :
        if sumValue > maxValue:
            maxValue = sumValue
        sumValue = 0

    else:
        if sumValue >= maxValue:
            maxValue = sumValue


print(maxValue)        
    