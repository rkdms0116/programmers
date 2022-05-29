import math

def solution(N, road, K):
    answer = 0
    # 탐색 여부
    detect_fir = [False for _ in range(N+1)]
    # 그래프
    delivery = [[False]*(N+1) for _ in range(N+1)]
    # 최소거리 저장
    min_fir = [math.inf for _ in range(N+1)]
    min_fir[1] = 0
    
    stack = [1]
    for info in road:
        if info[0] == 1:
            stack.append(info[1])
            min_fir[info[1]] = info[2]
        delivery[info[0]][info[1]] = info[2]
        delivery[info[1]][info[0]] = info[2]

    while stack:
        point = stack.pop(0)
        # 탐색을 안한 포인트라면
        if not(detect_fir[point]):
            detect_fir[point] = True
            for i in range(2, N+1):
                # 해당 그래프의 연결이 되어있고
                if delivery[point][i]:
                    weight = min_fir[point]
                    if weight + delivery[point][i] < min_fir[point]:
                        min_fir = weight + delivery[point][i]
                    if not(detect_fir[point]):
                        stack.append(point)
    print(min_fir)
            
    return answer

print(solution(5, [[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3))