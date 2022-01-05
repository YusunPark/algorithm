def solution(n):
    res = ''
    while n:
        n, r = divmod(n, 3)
        res += str(r)
    return int(res, base=3)
