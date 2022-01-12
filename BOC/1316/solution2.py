result = 0
for i in range(int(input())):
    word = input()
    print(list(word))
    print(sorted(word, key=word.find))
    if list(word) == sorted(word, key=word.lower):
        result += 1
print(result)