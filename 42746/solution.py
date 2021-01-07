data = [6, 10, 2]


def solution(numbers):
    return str(int(''.join(sorted(
        list(map(str, numbers)),
        key=lambda x: x * 3,
        reverse=True
    ))))


result = solution(data)
print(result)
