def solution(phone_book):
    phone_book.sort()
    print(phone_book)

    for i in range(len(phone_book)-1):
        word = phone_book[i] 
        if word in phone_book[i+1][:len(word)]:
            return False
    return True

result = solution([
    '119',
    '97674223',
    '1195524421'
])

print(result)
