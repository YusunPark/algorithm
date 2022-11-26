def add_time(day, term):
    day_split = day.split(":")
    year, month, day, h, m, s = [int(i) for i in day_split]

    term_split = term.split(":")
    tday, th, tm, ts = [int(i) for i in term_split]

    day += tday
    h += th
    m += tm
    s += ts

    if s >= 60:
        s -= 60
        m += 1
    
    if m >= 60:
        m -= 60
        h += 1

    if h >= 24:
        h -= 24
        day += 1

    if day >= 31:
        tmp_month = day // 30
        day %= 30
        month += tmp_month

    if month > 12:
        month -= 12
        year += 1

    return f"{year}:{month}:{day}:{h}:{m}:{s}"

def count_day(before, after):
    before_list = list(map(int, before.split(":")[:3]))
    after_list = list(map(int, after.split(":")[:3]))

    diff = []
    for a, b in zip(after_list, before_list):
        diff.append(a-b)
    
    for i, v in enumerate(diff):
        if v:
            if i == 0:
                diff[i+1] += (v*11)
                diff[i] = 0
            elif i == 1:
                diff[i+1] += (v*30)
                diff[i] = 0

    return diff[2]


def solution(s, times):
    answer = [1, 1]

    benchmark = s
    day = benchmark
    deposit = set([])

    for time in times:
        added = add_time(day, time)
        deposit.add(f'{added.split(":")[:3]}')
        day = str(added)

    d = count_day(benchmark, day)
    if len(deposit) == d: return [1, d+1]
    else: return [0, d+1]