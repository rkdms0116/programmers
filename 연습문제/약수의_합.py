def solution(n):
    answer = 0
    # 1부터 n까지의 수 중에서 나누어떨어지는 약수들을 answer에 더함
    for div in range(1,n+1):
        if not(n%div):
            answer += div
    return answer