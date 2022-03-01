def solution(participant, completion):    
    answer = ''
    dic = {}
    for person in participant:
        if person not in dic:
            dic[person] = 1
        else:
            dic[person] += 1
    for person in completion:
        if person in dic:
            dic[person] -= 1
    for key, val in dic.items():
        if val != 0:
            answer += key
    return answer
        
    # remove를 사용하면 시간초과 발생!!
    # for person in participant:
    #     if not person in completion:
    #         answer += person
    #     else:
    #         completion.remove(person)
    # return answer
    
    # for person in completion:
    #     if person in participant:
    #         participant.remove(person)

    # return "".join(participant)