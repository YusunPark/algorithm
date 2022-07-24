# input을 받으면서 개수 카운팅 해서 바로 삭제해버리기

n, m = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(int(input()))

run = True

while(run):
    prev = arr[0]
    tmp = [prev]
    count = 1

    for v in arr[1:]:
        if prev != v:
            if count >= m:
                for _ in range(count):
                    tmp.pop()                
            
            count = 1
            prev = v
        
        else:
            count += 1
        tmp.append(v)

    if count >= m:
        for _ in range(count):
            tmp.pop()

    if len(arr) == len(tmp) or len(tmp) == 0:
        run = False
    arr = tmp

print(len(tmp))
print("\n".join(map(str,tmp)))
