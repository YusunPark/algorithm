def solution(phone_book):
    phone_book.sort()
    
    for str1, str2 in zip(phone_book, phone_book[1:]):
        if str2.startswith(str1):
            return False
    return True

result = solution([
    '119',
    '97674223',
    '1195524421'
])

print(result)
