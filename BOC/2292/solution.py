
n = int(input())
i = 1


n = n - 1
while(1):
    if( n < 1 ):
        print(i)
        break
    else:
        n = n - (6*i)
        i += 1
