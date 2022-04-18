def solution(m, n, puddles):

    school = [[0]*(m+1) for _ in range(n+1)]
    school[1][1] = 1
    for i in range(1, n+1):
        for j in range(1, m+1):
            # 초기 설정값 (1,1) 이거나 puddles에 있는 값이면 pass
            if [i,j] == [1, 1] or [j,i] in puddles:
                continue
            else:
                school[i][j] = (school[i-1][j] + school[i][j-1])

    return school[-1][-1] % 1000000007