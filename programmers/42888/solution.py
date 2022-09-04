def solution(record):
    message = []
    user = {}
    actions = []

    for event in record:
        info = event.split()
        action, uid, *nickname = info
        if action in ['Enter', 'Change']:
            user[uid] = nickname[0]
        if action != 'Change':
            actions.append({'type': action, 'uid': uid})

    return [
        f'{user[action["uid"]]}님이 들어왔습니다.' if action['type'] == 'Enter' else f'{user[action["uid"]]}님이 나갔습니다.' 
        for action in actions
    ]
