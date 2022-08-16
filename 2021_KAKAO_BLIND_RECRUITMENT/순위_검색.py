from itertools import combinations

def solution(info, query):
    answer = []
    
    for quer in query:
        temp_con = quer.split()[:-1]
        score = quer.split()[-1]
        condition = ''
        for t in temp_con:
            if t != '-' and t != 'and':
                condition += t
        cnt = 0

        for i in info:
            info_temp = list(i.split()[:4])
            info_val = i.split()[-1]
            info_key = []
            if int(score) <= int(info_val):
                for k in range(5):
                    for combination in combinations(info_temp, k):
                        info_key.append(''.join(combination))
                if condition in info_key:
                    cnt += 1
        answer.append(cnt)
                        
    return answer

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))