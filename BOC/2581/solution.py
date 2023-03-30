import math 

m = int(input())
n = int(input())

sum_prime = 0
min_prime = 0

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: 
            return False
    
    return True

for i in range(m, n+1):
    if i == 1:
        continue
    if is_prime(i): 
        sum_prime += i
        if min_prime == 0:
            min_prime = i

if min_prime == 0:
    print(-1)
else:
    print(sum_prime)
    print(min_prime)

