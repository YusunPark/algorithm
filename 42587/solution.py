from collections import deque


def solution(priorities, location):
    order = 0

    documents = deque([
        (priority, index) for index, priority in enumerate(priorities)
    ])

    while len(documents):
        item = documents.popleft()
        if documents and max(documents)[0] > item[0]:
            documents.append(item)
        else:
            order += 1
            if item[1] == location:
                break

    return order


if __name__ == "__main__":
    test_cases = [
        ([2, 1, 3, 2], 2),
        ([1, 1, 9, 1, 1, 1], 0)
    ]

    for idx, case in enumerate(test_cases, start=1):
        result = solution(*case)
        print(f'{idx}번째 테스트: {result}')
