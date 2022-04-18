from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[False]*(n+1) for _ in range(n+1)]

    for ed in edge:
        graph[ed[0]][ed[1]] = True
        graph[ed[1]][ed[0]] = True
    visit = [False] * (n+1)
    stack = deque([1])
    le = 2
    while True:
        if stack:
            answer = len(stack)
            for p in range(len(stack)):
                np = stack[p]
                for i in range(n+1):
                    if graph[np][i] and visit[i] == False:
                        graph[np][i] = False
                        graph[i][np] = False
                        visit[i] = True
                        n_stack.append(i)
        else:
                le += 1
            else:
                break
                              
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))