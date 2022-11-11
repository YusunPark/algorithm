
depth_dic = {}
result = ''

def check(p, r):
    global result

    for v in depth_dic[p]:
        if v in depth_dic:
            check(v,  f'{r}/{v}')
        else:
            if len(f'{r}/{v}') > len(result):
                result = f'{r}/{v}'

    return


def solution(N, relation, dirname):
    depth = [0 for _ in range(N)]

    for parent, child in relation:
        name = dirname[parent-1]
        c_name = dirname[child-1]

        if name in depth_dic:
            tmp = depth_dic[name]
            tmp.append(c_name)
            depth_dic[name] = tmp
        else:
            depth_dic[name] = [c_name]


    check('root', 'root')
    return len(result)
