t = int(input())
s = ''


for i in range(t):
    command = input()
    d_command = command.replace("R", "")

    n = int(input())
    a = input()
    array = list(a[1:-1].split(","))

    if len(d_command) > n: s += 'error\n'
    elif "R" not in command: s += "["+",".join(array[len(d_command):])+"]\n"
    else:
        r_command = len(command)-len(d_command)
        forward, backward = 0, 0
        index = 0
        for i in range(1, r_command+1):
            if i % 2 == 1:
                forward += command[index:].index("R")
                index += command[index:].index("R")+1
            else:
                backward += command[index:].index("R")
                index += command[index:].index("R")+1

        if r_command % 2 == 1: 
            array.reverse()
            backward += (len(command)-index)
            if forward:
                s += "["+",".join(array[backward:-forward])+"]\n"
            else:
                s += "["+",".join(array[backward:])+"]\n"

        else : 
            forward += (len(command)-index)
            if backward:
                s += "["+",".join(array[forward:-backward])+"]\n"
            else:
                s += "["+",".join(array[forward:])+"]\n"


print(s[:-1])