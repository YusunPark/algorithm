n ,m = map(int, input().split())

a_pos = [0]
b_pos = [0]



# L : 0,  R: 1
dxs = [-1, 1]
direct = {'L' : 0, 'R': 1}

a_time = 0
for i in range(n):
    v, d = input().split()
    for j in range(int(v)):
        a_pos.append(a_pos[a_time] + dxs[direct[d]])
        a_time += 1

b_time = 0
for i in range(m):
    v, d = input().split()
    for j in range(int(v)):
        b_pos.append(b_pos[b_time] + dxs[direct[d]])
        b_time += 1


count = 0

for i in range(1, max(len(a_pos), len(b_pos))):
    if i >= len(a_pos):
        if a_pos[len(a_pos)-1] == b_pos[i]:
            count += 1
    elif i >= len(b_pos):
        if a_pos[i] == b_pos[len(b_pos)-1]:
            count += 1
    else:
        if a_pos[i] == b_pos[i] and a_pos[i-1] != b_pos[i-1]:
            count += 1
print(count)
