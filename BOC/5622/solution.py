dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = input()
result = 0

for i in alpha:
    str_match = list(filter(lambda x: i in x, dial))
    result += dial.index(str_match[0])+3
print(result)
    