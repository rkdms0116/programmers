def solution(d, budget):
    answer = 0
    # 부서별 신청 금액 오름차순으로 정렬
    d.sort()
    # 낮은 금액부터 합친 예산
    sub_bud = 0
    for i in range(len(d)):
        total_bud += d[i]
        # 예산을 넘어가면 break
        if total_bud > budget:
            break
        else:
            answer += 1
    return answer