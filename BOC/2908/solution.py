def change_num(number):
    first = number//100
    third = number%10
    number = number - ((first-third)*100) - (third-first)
    return number


a, b = map(int, input().split())

a = change_num(a)
b = change_num(b)

print(max(a,b))
# print(a) if a > b else print(b)