import sys
# shilt => 뒤에있는거를 앞으로 가져오는 것 밖에 없다.
s = input()
n = len(s)
s += s

min_len = sys.maxsize

for i in range(n, 2*n):
    result = ''
    prev = s[n-i]
    count = 1
    # print([s[n-i+j] for j in range(1, n)])

    for x in [s[n-i+j] for j in range(1, n)]:
        # print(x)
        if x == prev:
            count += 1
        else:
            prev = x
            result += prev + str(count)
            count = 1

    result += s[n-i-1] + str(count)
    # print(result)
    if min_len > len(result):
        min_len = len(result)

print(min_len)
