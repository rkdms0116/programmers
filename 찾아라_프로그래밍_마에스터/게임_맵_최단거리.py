from collections import deque


def solution(maps):    
    c = len(maps)
    r = len(maps[0])

    dy = [-1,1,0,0]
    dx = [0,0,-1,1]

    queue = deque()
    queue.append([0, 0])
    while queue:
        point = queue.popleft()
        y = point[0]
        x = point[1]

        if y == c-1 and x == r-1:
            return maps[y][x]

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if -1 < ny < c and -1 < nx < r  and maps[ny][nx] == 1:
                maps[ny][nx] = maps[y][x] + 1
                queue.append([ny, nx])


    return -1
