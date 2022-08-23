# 2 X 2 블록 찾는 함수
def combo(m,n,game):
    global answer
    dy = [1,1,0]
    dx = [0,1,1]
    combo_set = set()
    for j in range(m-1):
        for i in range(n-1):
            now = game[j][i]
            # now가 알파벳이 있다면
            if now:
                # 오른쪽, 아래, 왼쪽아래대각선이 now와 같은 값이라면 combo_set에 add
                for d in range(3):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if now != game[ny][nx]:
                        break
                else:
                    combo_set.add((i,j))
                    combo_set.add((i+1,j))
                    combo_set.add((i,j+1))
                    combo_set.add((i+1,j+1))
    # combo_set이 존재한다면, 존재하는 값들 False로 터트려주기!
    if combo_set:
        for x, y in combo_set:
            game[y][x] = False
            # 개수는 global 설정으로 추가
            answer += 1
        return game
    # combo_set이 존재하지 않는다면 while문 종료할 수 있도록 False return
    else:
        return False

# 중력 적용 함수
def gravity(m,n,game):
    for i in range(n):
        # 한 열의 존재하는 False의 개수
        cnt = 0
        # 아랫쪽부터 확인하면서 False라면 cnt ++
        for j in range(m-1,-1,-1):
            if not(game[j][i]):
                cnt += 1
            # 알파벳이고 cnt의 값이 존재한다면, False가 있었던 중력의 위치만큼 내려주기
            elif cnt > 0 and game[j][i]:
                now = game[j][i]
                game[j][i] = False
                game[j+cnt][i] = now
                    
def solution(m, n, board):
    global answer
    answer = 0
    game = [list(row) for row in board]
    # 2 X 2 블록 찾는 함수
    while combo(m,n,game):
        # 중력 적용
        gravity(m,n,game)
    return answer