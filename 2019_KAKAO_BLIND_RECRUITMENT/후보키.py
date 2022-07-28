from itertools import combinations

def solution(relation):
    # 후보키
    candidateKey = []
    # 가능한 조합의 개수
    comb = []
    for n in range(1, len(relation)+1):
        comb += list(combinations(list(i for i in range(len(relation[0]))), n))
    
    for com in comb:
        # 이미 후보키에 등록되어있는 조합인지 확인
        flag = True
        for i in candidateKey:
            com_set = set(com)
            if i.issubset(com_set):
                flag = False
                
        temp = []
        if flag:
            for row in range(len(relation)):
                # 사람의 성향을 넣어줌
                person = []
                for c in com:
                    person.append(relation[row][c])
                print(person)
                # 중복된다면 stop
                if person in temp:
                    print('stop')
                    break
                else:
                    temp.append(person)
                    
            # for문이 잘 끝났으면 후보키로 등록해주기
            else:
                candidateKey.append(set(com))

    return len(candidateKey)
