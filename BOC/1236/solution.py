from genericpath import exists


width, length = map(int, input().split(" "))

w_security = [0]*width
l_security = [0]*length
w_sum = 0
l_sum = 0

for i in range(width):
    security = input()
    for index, exist in enumerate(security):
        if exist == "X":
            l_security[index] = 1
            w_security[i] = 1
        else: pass

for i in w_security:
    if i == 0:
        w_sum += 1
for i in l_security:
    if i == 0:
        l_sum += 1



print(f'{max(w_sum,l_sum)}')
