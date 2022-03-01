s = input()
l = len(s)
while l:
    s = s.replace("()", "")
    l -= 1

print(len(s))
