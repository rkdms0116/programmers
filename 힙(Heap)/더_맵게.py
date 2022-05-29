def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        scoville.sort()
        # 두 개의 scoville의 값이 K값보다 작다면 -1 return
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        a = scoville[0]
        b = scoville[1]
        scoville = [a + 2*b] + scoville[2:]
        answer += 1
    return answer