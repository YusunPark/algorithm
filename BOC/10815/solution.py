n = int(input())
have = set(map(int, input().split(" ")))

m = int(input())
target = list(map(int, input().split(" ")))

result = ""
for x in target:
    if x in have: result += str(1) + ' '
    else: result += str(0) + ' '

print(result[:-1])