def solution(s):
    print(str(type(s)))
    if len(s) == 4 or len(s) == 6:
        try:
            s = int(s)
        except ValueError as e:
            return False 
     
        answer = True
        return answer
    answer = False
    return answer

s1 = "a234"
print(f"return : False => {solution(s1)}")

s2 = "1234"
print(f"return : True => {solution(s2)}")