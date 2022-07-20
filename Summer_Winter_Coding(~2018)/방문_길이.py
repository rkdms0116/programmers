def solution(dirs):
    position = set()
    x = y = 0
    for dir in dirs:
        # 방향에 따라 좌표 변환
        if dir == "L":
            nx = x-1
            ny = y
        elif dir == "R":
            nx = x+1
            ny = y
        elif dir == "U":
            nx = x
            ny = y - 1
        elif dir == "D":
            nx = x
            ny = y + 1
        # 좌표 위치가 유효한 범위 내에 있다면
        if -6 < nx < 6 and -6 < ny < 6:
            # 왕복은 같은 길이이므로
            position.add((x, y, nx, ny))
            position.add((nx, ny, x, y))
            x = nx
            y = ny
    # 왕복의 중복값 제거
    return len(position)//2
