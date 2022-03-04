global listA
global ListB

list0 = [0]*41
list1 = [0]*41

def fibo(n):
    if n == 0: 
        list0[n] = 1
        list1[n] = 0
        return
    if n == 1: 
        list0[n] = 0
        list1[n] = 1
        return
    else: 
        if list0[n] == 0:
            fibo(n-1)
            fibo(n-2)
            list0[n] = list0[n-1] + list0[n-2]
            list1[n] = list1[n-1] + list1[n-2]
            return
        else:
            pass


s = ''
for _ in range(int(input())):
    n = int(input())
    fibo(n)
    s += str(list0[n])+' '+str(list1[n])+'\n'

print(s[:-1])