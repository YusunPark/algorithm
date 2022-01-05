def solution(answers):
    
    num = []
    score = [0, 0, 0]
    # 1번
    student1 = [1, 2, 3, 4, 5]
    num.append(len(student1))
    
    # 2번
    student2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num.append(len(student2))
    
    # 3번
    student3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    num.append(len(student3))
    
    for idx, right in enumerate(answers):
        if right == student1[idx%num[0]]:
            score[0] += 1
        else: pass

    for idx, right in enumerate(answers):
        if right == student2[idx%num[1]]:
            score[1] += 1
        else: pass

    for idx, right in enumerate(answers):
        if right == student3[idx%num[2]]:
            score[2] += 1
        else: pass

        
    maxium = max(score)
    winner = []
    for i in range(3):
        if score[i] == maxium:
            winner.append(i+1)
        
    return winner

answers= [1, 2, 3, 4, 5]
print(solution(answers))