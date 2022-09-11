s = input()
t = input()

for _ in range(len(t)-len(s)):
    if t[-1] == 'A':
        t = t[:-1]
    else:
        t = t[::-1][1:]

if s == t:
    print(1)
else: print(0)
