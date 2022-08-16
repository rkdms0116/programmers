def solution(n):
    answer = [[0]*i for i in range(1, n+1)]
    num = 1
    # 시작 좌표
    x, y = 0, -1
    for cnt in range(n):
        for i in range(cnt, n):
            # 아래
            if cnt % 3 == 0:
                y += 1
            # 오른쪽
            elif cnt % 3 == 1:
                x +=1
            # 위
            else:
                x -= 1
                y -= 1
            answer[y][x] = num
            num += 1
    return sum(answer, list())
