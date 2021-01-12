def solution(number, k):
    stack = []
    for n in number:
        while len(stack) and k and stack[-1] < n:
            del stack[-1]
            k -= 1
        stack.append(n)
    return ''.join(stack[:-k] if k else stack)


if __name__ == "__main__":
    data = [
        ('1924', 2),
        ('1231234', 3),
        ('4177252841', 4)
    ]
    for i, case in enumerate(data, start=1):
        print(f'{i}번째 테스트: {solution(*case)}')

