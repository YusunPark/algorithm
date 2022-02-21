def hanoi_xy(x,y,count):
    print("1 2")
    print(x)
    y.append(x.pop())
    print(x)
    print(y)
    count += 1

def hanoi_xz(x,z,count):
    print("1 2")
    print(x)
    z.append(x.pop())
    print(x)
    print(z)
    count += 1

def hanoi_yz(y,z,count):
    print("1 2")
    print(x)
    z.append(x.pop())
    print(x)
    print(z)
    count += 1


        



n = int(input())
x = []
y = []
z = []
count = 0

for i in range(1, n+1):
    x.append(i)

hanoi_xy(x,y,count)


