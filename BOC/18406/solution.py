n = list(input())

left = n[:len(n)//2]
right = n[len(n)//2:]

sum_l = sum(list(map(int, left)))
sum_r = sum(list(map(int, right)))

if sum_l == sum_r : print("LUCKY")
else : print("READY") 