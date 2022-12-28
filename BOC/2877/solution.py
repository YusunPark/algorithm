# 2 : 0 1 
# 4 : 00 01 10 11
# 8 : 000 001 010 011 100 101 110 111

k = int(input())
i = 2
count = 1
while(k > i):
    k -= i
    i *= 2
    count += 1

binary = str(bin(k-1)).split("0b")[1]
if count > len(binary):
    tmp = "0" * (count-len(binary))
    binary = tmp + binary

print("".join(["4" if x == "0" else "7" for x in binary]))