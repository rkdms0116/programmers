def solution(a, b):
    answer = 0
    # 최솟값을 n, 최댓값을 m으로 지정
    n, m = min(a, b), max(a, b)
    # answer에 사이에 있는 값들을 더해줌
    for num in range(n, m+1):
        answer += num
    return answer