i = input()

if(i[2] == ' '):
    pass
else:

    num, str = i.split()
    num = int(num)
    output = ''

    for s in str:
        output += s*num

    print(output)