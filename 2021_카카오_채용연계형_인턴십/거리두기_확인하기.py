# 방향
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

def solution(places):
    answer = []

    for place in places:
        result = 1
        # 이중 for문으로 대기방의 모든 것을 탐색
        for r in range(5):
            for c in range(5):
                # 응시자가 있다면
                if place[c][r] == 'P':
                    # 상하좌우 탐색
                    for i in range(4):
                        nc = dc[i] + c
                        nr = dr[i] + r
                        # 인덱스가 정해진 범위 안에 있고 X(가림막)가 아닐 때만 확인
                        if -1 < nc < 5 and -1 < nr < 5 and place[nc][nr] != "X":
                            tc = nc
                            tr = nr
                            cnt = 0
                            # 만약에 P(응시자)가 있다면 result 0
                            if place[nc][nr] == "P":
                                result = 0
                                break
                            # 응시자가 없다면 한 번 더 상하좌우를 살펴주는데 상하좌우 중에 P가 무조건 한 개 있고, 그 이상 있는지 체크
                            for k in range(4):
                                nc = dc[k] + tc
                                nr = dr[k] + tr
                                if -1 < nc < 5 and -1 < nr < 5 and place[nc][nr] == "P":
                                    cnt += 1
                            # P가 1개 이상이면 거리두기 불가능!
                            if cnt != 1:
                                result = 0
                                break
        answer.append(result)
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))