arr = map(int, input().split())
temp = []

for i, n in enumerate(arr):
    if n >= 250:
        break
    
    temp.append(n)
 
print(sum(temp), round(sum(temp)/len(temp),1))  