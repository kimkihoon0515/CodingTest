def solution(board):
    answer = 0
    if len(board) == 1: # board의 행이 1개일 경우에는 무조건 길이 1짜리 정사각형이 나오므로 
        answer = 1
    else:
        for i in range(1,len(board)):
            for j in range(1,len(board[0])):
                if board[i][j] == 1:
                    board[i][j] = min(board[i][j-1],board[i-1][j],board[i-1][j-1])+1 # i,j값까지의 정사각형형의 한 변의 길이를 갱신하는데 그 전 단계 +1이므로
                answer = max(answer,board[i][j])  # 최대값이 answer이다.
    return answer **2