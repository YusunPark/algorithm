
def run(n, m, card):
    minRow = 0
    for  row in card:
        if minRow < min(row):
             minRow = min(row)
    print(minRow)

    

n = 3
m = 3
card = [[3,1,2], [4,1,4], [2,2,2]]

run(n, m, card)


n = 2
m = 4
card = [[7,3,1,8], [3,3,3,4]]

run(n, m, card)

