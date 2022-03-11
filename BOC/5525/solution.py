n = int(input())
m = int(input())
s = input()
p = 'IOI'
count = 0

for i in range(n-1):
    p += 'OI'
    
for i, sc in enumerate(s):
    if sc == 'I':
        if s[i:i+(n*2+1)] == p:
            count += 1
print(count)