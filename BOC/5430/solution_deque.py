from collections import deque

t = int(input())
s = ''

for i in range(t):
    command = input()
    d_command = command.replace("R", "")
    n = int(input())
    a = input()
    array = deque(a[1:-1].split(","))
    direct = 1
    if len(d_command) > n: s += 'error\n'
    else:
        for i in command:
            if i == "R": direct += 1
            else :
                if direct % 2 == 0 : array.pop()
                else: array.popleft()
        if direct % 2 == 0: 
            array.reverse()
        s += "["+",".join(array)+"]\n"

print(s[:-1])