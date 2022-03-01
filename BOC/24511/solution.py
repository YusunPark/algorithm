from sys import stdin
# n = int(input())
n = int(stdin.readline())

# qs = list(map(int, input().split(" ")))
qs = list(map(int, stdin.readline().split()))

# container = list(map(int, input().split(" ")))
container = list(map(int, stdin.readline().split()))


# m = input()
m = int(stdin.readline())

# c = list(map(int, input().split(" ")))
c = list(map(int, stdin.readline().split(" ")))

array = [0]*m

for i in range(m):
    result = c[i]
    for j in range(n):
        if qs[j] == 1:
            pass
        else:
            result, container[j] = container[j], result
    array[i] = result

s = ""
for i in array:
    s += (str(i) + ' ')
print(s)