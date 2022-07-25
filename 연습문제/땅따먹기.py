def solution(land):
    for i in range(1, len(land)):
        for j in range(len(land[0])):
            # 윗 행의 현재 있는 열을 제외하고 최댓값을 더해줌
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1:])
    # 마지막에서 가장 큰 값을 return
    return max(land[-1])
