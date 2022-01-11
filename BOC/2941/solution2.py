a = input()
cro =['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
for x in cro:
    a = a.replace(x, '1')
print(len(a))