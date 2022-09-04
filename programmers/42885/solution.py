def solution(people, limit):
    people.sort(reverse=True)

    counter = len(people)

    s = 0
    e = counter - 1

    while s < e:
        if people[s] + people[e] <= limit:
            e -= 1
            counter -= 1
        s += 1
    
    return counter


if __name__ == "__main__":
    test_cases = [
        ([70, 50, 80, 50], 100),
        ([70, 80, 50], 100)
    ]
    
    for case in test_cases:
        result = solution(*case)
        print(result)
