n = int(input())

left = 0
right = 0
l_max = 0
r_max = 0

height = []

for i in range(n):
    height.append(int(input()))

for i in range(n):
    if l_max < height[i]:
        l_max = height[i]
        left += 1
    else: pass
    if r_max < height[n-i-1]:
        r_max = height[n-i-1]
        right += 1
    else: pass

print(left)
print(right)
