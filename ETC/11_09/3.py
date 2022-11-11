import math

def solution(n):
    factorial_value = str(math.factorial(n))    
    tail_value = factorial_value[-1]
    count = 0 
    
    for v in reversed(factorial_value):
        if v == tail_value:
            count += 1
        else: break

    return count

# memo = {}

# def factorial(n):
#     global memo
#     if n in memo:
#         return memo[n]
#     elif n <= 1:
#         return 1
#     else:
#         memo[n] = n * factorial(n-1)
#         return memo[n]
    

# def solution(n):
#     factorial_value = n * factorial(n-1) if n > 1 else 1
#     print(factorial_value)
#     factorial_value = str(factorial_value)
    
#     tail_value = factorial_value[-1]
#     count = 0 
    
#     for v in reversed(factorial_value):
#         if v == tail_value:
#             count += 1
#         else: break

#     return count
    