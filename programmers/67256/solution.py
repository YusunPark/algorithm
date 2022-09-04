keypad = {
    1:(0,0), 2:(0,1), 3:(0,2),
    4:(1,0), 5:(1,1), 6:(1,2),
    7:(2,0), 8:(2,1), 9:(2,2),
    '*':(3,0), 0:(3,1), '#':(3,2)
}


def find_distance(target, current_key):
    distance = {'left': 0, 'right': 0}
    for hand, pos in current_key.items():
        target_pos = keypad[target]
        current_pos = keypad[current_key[hand]]
        distance[hand] = abs(target_pos[0] - current_pos[0]) + abs(target_pos[1] - current_pos[1])
    return distance


def touch(target, current_key, hand):
    if target in [1, 4, 7]:
        current_key['left'] = target
        return 'L', current_key
    elif target in [3, 6, 9]:
        current_key['right'] = target
        return 'R', current_key
    else:
        distance = find_distance(target, current_key)
        if distance['left'] < distance['right']:
            current_key['left'] = target
            return 'L', current_key
        elif distance['left'] > distance['right']:
            current_key['right'] = target
            return 'R', current_key
        else:
            if hand == 'left':
                current_key['left'] = target
                return 'L', current_key
            else:
                current_key['right'] = target
                return 'R', current_key


def solution(numbers, hand):
    answer = ''
    current_key = {
        'left': '*',
        'right': '#'
    }

    for i, number in enumerate(numbers, start=1):
        h, current_key = touch(number, current_key, hand)
        answer += h

    return answer
