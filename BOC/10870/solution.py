def fibo5(n):
    if n <= 1:
        return n
    return fibo5(n-1)+fibo5(n-2)




n = int(input())
print(fibo5(n))


# 재귀함수를 피하는 방법
fibo = [0.1]
for i in range(2, n+1):
    fibo.append(fibo[i-2]+fibo[i-1])