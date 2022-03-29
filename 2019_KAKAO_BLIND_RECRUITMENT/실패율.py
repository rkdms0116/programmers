def solution(N, stages):
    answer = []
    dic = {}
    challenger = len(stages)
    
    for level in range(1,N+1):
        if challenger:
            dic[level] = stages.count(level)/challenger
        else:
            dic[level] = 0
        challenger -= stages.count(level)
    
    sorted_dic = sorted(dic.items(), key = lambda item: item[1], reverse = True)
    for n in range(len(sorted_dic)):
        answer.append(sorted_dic[n][0])
    
    return answer