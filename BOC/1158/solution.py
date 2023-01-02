n, k = map(int, input().split())

arr = [i for i in range(1, n+1)]
result = []
d = 0

while(arr):
    d = (d+k-1) % len(arr)
    result.append(arr[d])
    del arr[d]

print("<"+", ".join(map(str,result))+">")


