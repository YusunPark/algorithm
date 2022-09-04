def solution(skill, skill_trees):
    counter = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)

        for s in skill_tree:
            if s in skill and s != skill_list.pop(0):
                break
        else:
            counter += 1

    return counter


if __name__ == "__main__":
    for case in [
        ('CBD', ["BACDE", "CBADF", "AECB", "BDA"])
    ]:
        result = solution(*case)
        print(result)
