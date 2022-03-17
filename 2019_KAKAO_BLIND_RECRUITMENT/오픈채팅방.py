def solution(record):
    answer = []
    u_nick = {}
    for cnt in range(len(record)):
        if record[cnt][0] == "E" or record[cnt][0] == "C":
            state, uid, nick = map(str, record[cnt].split())
            u_nick[uid] = nick
    
    for cnt in range(len(record)):
        if record[cnt][0] == "E":
            state, uid, nick = map(str, record[cnt].split())
            nickname = u_nick[uid]
            answer.append(nickname + "님이 들어왔습니다.")
        elif record[cnt][0] == "L":
            state, uid = map(str, record[cnt].split())
            nickname = u_nick[uid]
            answer.append(nickname + "님이 나갔습니다.")
    return answer