def binary(array, low, high, value):
    if low > high:
        return 0
    else:
        middle = (low+high)//2
        
        if array[middle] == value:
            return 1
        elif array[middle] > value:
            return binary(array, low, middle-1, value)
        else:
            return binary(array, middle+1, high, value)
        return 0


n = int(input())
a = list(map(int,input().split(" ")))
a.sort()

m = int(input())
b = list(map(int,input().split(" ")))


for x in b:
    print(binary(a, 0, len(a)-1, x))
    