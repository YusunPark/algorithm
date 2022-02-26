score = [0]
index = 0

for i in range(10):
    mushroom = int(input())
    score.append(score[i]+mushroom)
    if score[i+1] <= 100:
        index = i+1

if index == 10:
    print(score[index])

else:
    if score[index] == 100:
        print(100)
    elif (100-score[index]) < (score[index+1]-100):
        print(score[index])
    else:
        print(score[index+1])



