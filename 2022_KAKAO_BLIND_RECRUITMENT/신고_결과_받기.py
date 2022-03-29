def solution(id_list, report, k):
    answer = []
    # 알림이 가는 유저
    alert = {}
    # warn = {신고당한 유저 : [신고한 유저들], }
    warn = {}
    for idL in id_list:
        warn[idL] = []
        alert[idL] = 0
        
    for rep in report:
        user1, user2 = map(str, rep.split())
        if user2 in warn:
            if user1 in warn[user2]:
                pass
            else:
                warn[user2].append(user1)
    
    # 신고한 유저들에게 알람 +
    for w in warn:
        if len(warn[w]) >= k:
            for call in warn[w]:
                alert[call] += 1
    
    for peo in alert:
        answer.append(alert[peo])
        
    return answer