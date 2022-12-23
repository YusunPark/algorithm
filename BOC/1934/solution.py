def gcd(x, y):
    while(y):
        x, y = y, x%y
    return x

def lcm(x,y):
    result = (x*y)//gcd(x,y)
    return result

for _ in range(int(input())):
    a,b = map(int, input().split())
    print(lcm(a,b))