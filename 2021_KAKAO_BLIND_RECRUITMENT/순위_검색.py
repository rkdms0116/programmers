def solution(info, query):
    answer = []
    # query에 있는 조건 하나씩 뽑아서 list에 담기
    conditions = [quer.split() for quer in query]
    for condition in conditions:
        # and 없애기
        condition.pop(1)
        condition.pop(2)
        condition.pop(3)
        # 조건에 맞는 인원 count
        cnt = 0
        # 사람들의 정보를 탐색
        for i in info:
            # 
            person = list(i.split())
            for p in range(len(person)):
                if person[p] == "-":
                    pass
                elif person[p] != condition[p]:
                    break
            else:
                cnt += 1
        answer.append(cnt)
        
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))