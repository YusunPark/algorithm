number = input()

count = len(number)
number = number.replace('6','').replace('9','')
count -= len(number)
count = (count+1) // 2 

for i in range(9):
  if i == 6 :
    continue
  tmp_count = len(number)
  number = number.replace(f'{i}','')
  tmp_count -= len(number)
  if count < tmp_count:
    count = tmp_count


print(count)
