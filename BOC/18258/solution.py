from sys import stdin


n = int(stdin.readline())

array = []
s = ''
count = 0
index = 0

for i in range(n):
    command =  stdin.readline().split("\n")[0]
    if 'push' in command:
            array.append(command.split(" ")[1])
            count += 1
    elif count == 0:
        if 'size' in command: s += '0\n'
        elif 'empty' in command:s += '1\n'
        else: s += '-1\n'
    else:
        if 'pop' in command:
            s += (array[index] + '\n') 
            count -= 1
            index += 1
  
        elif 'size' in command: s += (str(count) + '\n') 

        elif 'empty' in command: s += ('0\n')     

        elif 'front' in command :s += (array[index] + '\n') 

        else: s += (array[-1] + '\n') 

print(s[:-1])