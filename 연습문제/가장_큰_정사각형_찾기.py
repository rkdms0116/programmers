def solution(board):
    answer = 0
    if len(board) < 2 and 1 in board[0]:
        return 1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j]:
                board[i][j] = min(board[i-1][j-1], board[i-1][j], board[i][j-1]) + 1
                answer = max(answer, board[i][j])
    return answer**2
board = [[1]]
solution(board)
print(board)