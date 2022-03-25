n, m, k = map(int, input().split(" "))
array = list(map(int, input().split(" ")))

array.sort()

max_value = array.pop()


total = max_value * (k * ( m // (k + 1)) + (m %(k + 1)))
total += (array.pop() * ( m // (k+1)))
print(total)
