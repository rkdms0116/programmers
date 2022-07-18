def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    dx = [0, 1, -1]
    dy = [1, 0, -1]
    x = 0
    y = -1
    d = 0
    cnt = 1
    while True:
        if cnt == n*(n+1)/2:
            break
        d %= 3
        ny = y + dy[d]
        nx = x + dx[d]
        try:
            if answer[ny][nx] == 0:
                answer[ny][nx] = cnt
                cnt += 1
        except IndexError:
            d += 1
        
    return answer

print(solution(4))