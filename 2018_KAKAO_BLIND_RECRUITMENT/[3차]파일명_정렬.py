def solution(files):
    answer = []
    temp = []
    for file in files:
        # 글자가 한 번 나타났다면 False로 변경
        flag = True
        for f in range(len(file)):
            # 숫자가 나타나기 전까지 head, 이후 부분을 num_tail, 숫자 등장으로 flag는 False로
            if flag and file[f].isdigit():
                head = file[:f]
                num_tail = file[f:]
                flag = False
                # num_tail부분을 돌면서 number와 tail 부분 쪼개기 
                for j in range(len(num_tail)):
                    if not(num_tail[j].isdigit()):
                        num = num_tail[:j]
                        tail = num_tail[j:]
                        break
                # num_tail의 모든 부분이 숫자였다면 그대로 num에
                else:
                    num = num_tail
                    tail = ''
        temp.append([head,num,tail])
    # head부분에 따라 정렬 및 number에 따라 정렬    
    temp.sort(key = lambda x:(x[0].lower(), int(x[1])))
    # join해서 answer에 대입
    for t in temp:
        answer.append(''.join(t))
    return answer
