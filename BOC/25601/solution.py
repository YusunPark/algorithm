import sys

n = int(input())

dict = {}

for _ in range(n-1):
    child, parent = input().split()
    dict[child] = parent

a, b = input().split()

# a부터 탐색
key = a
while (1):
    if key in dict:
        if b == dict[key]:
            print(1)
            sys.exit()
        else:
            key = dict[key]
    else:
        break

key = b
while (1):
    if key in dict:
        if a == dict[key]:
            print(1)
            sys.exit()
        else:
            key = dict[key]
    else:
        break


print(0)
