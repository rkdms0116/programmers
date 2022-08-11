def solution(msg):
    answer = []
    # 사전에 A~Z까지 영어를 key, 번호를 value로 갖게
    idx_dic = {}
    for i in range(65, 91):
        idx_dic[chr(i)] = i-64
    # 시작 index
    idx = 0
    # 사전의 value값(len으로 해도 되지만!)
    n = 27
    # idx부터 볼 뒤의 값
    s = 1
    
    # 찾는 idx가 msg의 길이가 될 때까지 실행
    while idx < len(msg):
        # 사전에 있다면, 뒤에 값을 더 확인하기 위하여 s값 ++
        if msg[idx:idx+s] in idx_dic:
            s += 1
            # 만일 길이까지 넘치게 된다면, 두 가지 경우가 나옴!
            if idx+s-1 == len(msg):
                # idx부터 쭉 값을 확인할 수 있거나
                if msg[idx:] in idx_dic:
                    answer.append(idx_dic[msg[idx:]])
                # 마지막 한 글자는 사전에 없기 때문에 따로 봐주거나
                else:
                    answer.append(idx_dic[msg[idx:idx+s]])
                    answer.append(idx_dic[msg[-1]])
                return answer
        # 사전에 없는 값이 된다면
        else:
            # 그 전까지의 msg를 잘라서 answer에 추가
            answer.append(idx_dic[msg[idx:idx+s-1]])
            # 사전에 그 뒤에 알파벳까지 추가해서 넣어줌
            idx_dic[msg[idx:idx+s]] = n
            # 사전의 len(value) 값 증가, index는 s-1까지 볼 수 있었으므로 추가, idx 뒤에 볼 s값 1로 초기화
            n += 1
            idx += s-1
            s = 1
