import re

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

a = input()


for x in croatia:
    a =  re.sub(x,"1", a)

print(len(a))