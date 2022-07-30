def solution(n):
    ans = 0
    # 거꾸로 생각해서 2로 계속 나누면서(건전지 사용 X) 나머지(점프해야하는 개수)에서는 ans ++
    while n > 0:
        if n % 2:
            ans += 1
        n //= 2
    return ans

