n, k = map(int, input().split())

count = 0


def num2str(num):
    if num < 10:
        return "0"+str(num)
    else:
        return str(num)


for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if str(k) in num2str(h)+num2str(m)+num2str(s):
                count += 1

print(count)
