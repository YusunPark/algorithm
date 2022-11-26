import datetime

def solution(s, times):
    benchmark = datetime.datetime.strptime(s,'%Y:%m:%d:%H:%M:%S')
    day = benchmark
    deposit = set([])
    
    for time in times:
        t = list(map(int, time.split(":")))
        term = datetime.timedelta(days=t[0], hours=t[1], minutes=t[2], seconds=t[3])
        day = day + term
        deposit.add(day.date())

    d = day.date() - benchmark.date()

    if len(deposit) == d.days: return [1, d.days+1]
    else: return [0, d.days+1]
