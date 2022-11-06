def solution(a, b, n):
    answer = 0
    while a <= n:
        # 몫과 나머지
        q, r = divmod(n,a)
        # 몫의 개수 만큼 b개로 return
        n = q*b + r
        answer += q*b
    return answer