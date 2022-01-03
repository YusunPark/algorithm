count = 0;
a = []

while(count < 10):
    i = int(input())%42
    a.append(i)
    count += 1

print(len(list(set(a))))