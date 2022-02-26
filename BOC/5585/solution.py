import math

spent = int(input())
change = 1000-spent
count = 0

if spent == 1000:
    print(0)
else:
    for i in range(math.ceil(math.log10(change+1))):
        coin = change%10
        change = change//10
        count = count + (coin//5) + (coin%5)


    print(count)
