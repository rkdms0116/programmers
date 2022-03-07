def solution(n):
    answer = ''
    while n:
        # 3으로 나누어 떨어지지 않는 경우
        if n%3:
            # answer에 나머지를 더하구 n은 3으로 나눈 몫으로 변환
            answer += str(n%3)
            n //= 3
        # 3으로 나누어 떨어지는 경우 (3:4, 6:14, 9:24)
        else:
            # n에 4를 대입하고 n은 3으로 나눈 몫에서 1을 뺀 값으로 변환
            answer += '4'
            n = n//3 -1
    return answer[::-1]