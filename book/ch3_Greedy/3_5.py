
def run(n, k, c):
    if n == 1:
        print(c)
        return 
    if n % k == 0: # 나눈어 떨어지는 경우
        return run(n/k , k, c+1)
    else: 
        return run(n-1, k, c+1)




n, k = 25, 3
count = 0
run(n, k, count)