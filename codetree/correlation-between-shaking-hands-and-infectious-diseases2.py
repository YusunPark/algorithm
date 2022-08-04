n, k, p, t = map(int, input().split())

log = [
    list(map(int, input().split()))
    for _ in range(t)
]
person = [0]*n
p_list = {p}
log.sort()

for v in log:
    for pp in p_list.copy():
        
        if pp in v[1:]: # 악수한 사람 중 감염자 존재
            if person[pp-1] == k: # k명을 감염 시켰으면 더이상 감염 x
                continue
            else:
                for i in v[1:]:  # 감염 당한 사람 찾기
                    if i != pp:
                        p_list.add(i)
                        person[pp-1] += 1

result = ''
for i in range(1, n+1):
    if i in p_list.copy():
        result += '1'
    else:
        result += '0'       

print(result)
