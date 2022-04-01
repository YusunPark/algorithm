n = int(input())
time = list(map(int, input().split(" ")))

time.sort()

total = 0
prev_time = 0

for i in time:
    prev_time += i
    total += prev_time
print(total)