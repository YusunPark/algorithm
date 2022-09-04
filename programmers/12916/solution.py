def solution(s: str) -> bool:
    return s.lower().count('p') == s.lower().count('y')


if __name__ == "__main__":
    for case in ['pPoooyY', 'Pyy']:
        result = solution(case)
        print(result)