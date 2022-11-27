for i in range(int(input())):
    formula = list(input().split())
    value = float(formula[0])
    del formula[0]
    
    for cmd in formula:
        if cmd == '@':
            value *= 3
        elif cmd == '%':
            value += 5
        elif cmd == '#':
            value -= 7
        else: pass
    print("{:.2f}".format(value))
