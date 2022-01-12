count = int(input())
result = 0

for n in range(count) : 

    a = input()
    b  = a + '0'


    for i, x in enumerate(a):
        if i == len(a)-1:
            result += 1

        elif x == b[i+1]:
            pass

        elif x in a[i+2:] : 
            break;

        else : pass

print(result)


    # print([pos for pos, char in enumerate(a) if char == 'a'])