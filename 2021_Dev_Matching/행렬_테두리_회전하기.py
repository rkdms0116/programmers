def solution(rows, columns, queries):
    answer = []
    # 1. row * column 행렬 만들기
    arr = []
    for r in range(rows):
        arr.append(list(columns*r+c for c in range(1, columns+1)))

    # 2. 회전
    for query in queries:
        x1, y1, x2, y2 = query
        mini = temp = arr[x1-1][y1-1]
        for a in range(y1, y2):

            arr[x1-1][a], temp = temp, arr[x1-1][a]    

            if temp < mini:
                mini = temp

        for b in range(x1, x2):
            
            arr[b][y2-1], temp = temp, arr[b][y2-1]

            if temp < mini:
                mini = temp
        
        for c in range(y2-2, y1-2, -1):

            arr[x2-1][c], temp = temp, arr[x2-1][c]

            if temp < mini:
                mini = temp
        
        for d in range(x2-2, x1-1, -1):

            arr[d][y1-1], temp = temp, arr[d][y1-1]

            if temp < mini:
                mini = temp
                
        arr[x1-1][y1-1] = temp

        # 3. 최솟값 
        answer.append(mini)

    return answer