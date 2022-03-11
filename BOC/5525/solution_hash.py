n = int(input())
m = int(input())
s = input()
p = 'IOI'
count = 0

for i in range(n-1):
    p += 'OI'


while(1):

    if s.find('I') == -1:
        break
    else: 
        if s[s.find('I'):s.find('I')+(n*2+1)] == p: 
            s = s[s.find('I')+2:]
            count += 1
        else:
            s = s[s.find('I')+1:]
        
print(count)
