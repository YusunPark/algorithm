num = int(input())

for n in range(num):
    count, str = input().split()
    count = int(count)
    output = ''
    for s in str:
        output += s*count
    print(output)