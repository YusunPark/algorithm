str = input().upper()

dict = {}

for s in str:
    if(dict.get(s)):
        dict[s] += 1
    else:
        dict[s] = 1

if(len([k for k,v in dict.items() if max(dict.values()) == v]) > 1):
    print('?')

else:
    max_key = max(dict, key=dict.get)
    print(max_key)