def palindrome(number):
    for i in range(len(number)//2):
        if number[i] != number[-(i+1)]:
            return 'no'
    return 'yes'

stop = True
result = ''

while(stop):
    n = input()
    if n == '0':
        stop = False
    else:
        result += f'{palindrome(n)}\n'
print(result[:-1])