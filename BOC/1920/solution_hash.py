# 해시 : 48964ms, 192ms

n = int(input())
a = list(map(int,input().split(" ")))
m = int(input())
b = list(map(int,input().split(" ")))

hash_a = set(a)

for x in b: #o(m)
    if x in hash_a: #o(1)
        print(1)
    else: print(0)


