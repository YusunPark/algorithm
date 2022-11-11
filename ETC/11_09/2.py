import math
import itertools

def solution(n):
    k = 0
    binary_str = ''
    result = 0
    answer  = -1

    while(n):   
        if n % 2 == 1:
            k += 1
            binary_str = '1' + binary_str
        else:
            binary_str = '0' + binary_str

        n = n // 2
    
    while(binary_str.count('1') != 1):
        result += math.comb(len(binary_str)-1, k)   

        k -= 1 
        index = binary_str[1:].find('1') + 1
        binary_str = binary_str[index:]

    result += len(binary_str) -1
    
    return result