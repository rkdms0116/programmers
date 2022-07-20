def solution(skill, skill_trees):
    answer = 0
    # skill_trees에 있는 skill을 skills란 이름으로 한개씩 뽑음
    for skills in skill_trees:
        # skill에 있는 index를 순차적으로 봐주기 위해
        idx = 0
        for s in skills:
            if s in skill:
                # 순서대로가 아니라면 for문을 break
                if skill[idx] != s:
                    break
                # 순서대로라면 index +1
                else:
                    idx += 1
        # for문을 정상적으로 마쳤을경우 answer +1
        else:
            answer += 1
    return answer
