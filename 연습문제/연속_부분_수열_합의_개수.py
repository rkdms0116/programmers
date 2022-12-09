# 시간 초과
def solution(elements):
    # 합을 저장하는 set
    sum_set = set()
    
    # 원형 수열
    que = elements * 2
    cnt = 1
    for _ in range(len(elements)):
        for idx in range(len(elements)):
            if cnt == len(elements)+1:
                break
                
            temp_sum = 0
            for c in range(cnt):
                temp_sum += que[idx+c]

            sum_set.add(temp_sum)
        else:
            cnt += 1

    return len(sum_set)

# pass code
def solution(elements):
    # 합을 저장하는 set
    sum_set = set()
    
    # 원형 수열
    que = elements * 2
    # 시작하는 index
    for i in range(len(elements)):
        # slice의 범위
        for j in range(1, len(elements)+1):
            sum_set.add(sum(que[i:i+j]))

    return len(sum_set)