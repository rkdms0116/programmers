def solution(priorities, location):
    answer = 0
    
    # index 번호와 순서를 담을 list 생성
    idx = [i for i in range(len(priorities))]
    turn = []
    
    cnt = 0
    while cnt != len(priorities):
        # priorities의 최댓값을 찾아서 M_pri에 저장
        M_pri = max(priorities)
        for pri in range(len(priorities)):
            # priorities를 돌면서 최댓값과 같아진다면 해야할 일
            if priorities[pri] == M_pri:
                # cnt ++, turn에 해당 index 넘버 추가, priorities의 최댓값을 발견한것이므로 0으로 바꿔줌
                cnt += 1
                turn.append(idx[pri])
                priorities[pri] = 0
                # priorities와 idx를 쪼개서 붙여줌 
                priorities = priorities[pri:] + priorities[:pri]
                idx = idx[pri:] + idx[:pri] 
                # for문을 더 돌 이유가 없으므로 break!
                break
    # turn에서 내가 찾고자하는 location이랑 같다면 몇 번째(+1)에 해당하는지가 answer
    for t in range(len(turn)):
        if turn[t] == location:
            answer = t+1
    return answer