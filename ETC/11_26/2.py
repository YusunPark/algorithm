def solution(id_list, k):
    customer_id = {}        

    for id_str in id_list:
        id_set = set(id_str.split())
        for i in id_set:
            if i in customer_id: customer_id[i] += 1
            else: customer_id[i] = 1

    answer = 0
    for customer, total in customer_id.items():
        if total >= k:
            answer += k
        else:
            answer += total

    return answer