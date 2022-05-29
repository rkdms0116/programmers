def solution(n):
    answer = 0
    # 1은 소수가 아니므로 n에서 2부터 n까지 check
    for num in range(2, n+1):
        # 나누어지는 수의 개수 check
        div = 0
        # 1부터 num의 제곱근까지 돌면서
        for i in range(1, int(num**(1/2)+1)):
            # num을 i로 나누어떨어질 때 div ++, div == 2면 소수가 아니므로 num에 대한 검사 중지
            if not(num%i):
                div += 1
                if div == 2:
                    break
        else:
            answer += 1

    return answer

