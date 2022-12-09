def solution(board):
    answer = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if i==0 or j==0:
                pass
            elif board[i][j] and board[i][j-1] and board[i-1][j] and board[i-1][j-1]:
                board[i][j] = board[i-1][j-1] +1
            answer = max(answer, board[i][j])
    print(board)
    return answer**2


print(solution([[0,0,0],[0,0,0]]))
print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]]))
print(solution([[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [0, 0, 1, 0]]))