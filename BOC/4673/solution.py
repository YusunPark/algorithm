def self_num(number, list):
    target =  number + sum(map(int, str(number)))
    if(target in list):
        total.remove(target)
        return list
    else:
        return list



total = [i for i in range(1, 10000)]

for num in range(1,10000):
    self_num(num, total)

for i in total:
    print(i)
