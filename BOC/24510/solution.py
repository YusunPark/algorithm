max_ = 0
word = ['for', 'while']

for _ in range(int(input())):
    str = input()
    count = 0
    i = 0;
    while(i < len(str)):
        if str[i] == 'f':
            if str[i:i+3] == word[0]:
                count += 1
                i += 1
        
        elif str[i] == 'w':
            if str[i:i+5] == word[1]:
                count += 1
                i += 3
        
        i += 1

    if count > max_:
        max_ = count
print(max_)
            


