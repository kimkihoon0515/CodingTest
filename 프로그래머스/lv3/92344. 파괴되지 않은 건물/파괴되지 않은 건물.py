
def solution(board, skill):
    answer = 0
    n = len(board)
    m = len(board[0])
    tmp = [[0 for i in range(m+1)] for _ in range(n+1)] 
    
    for t,r1,c1,r2,c2,degree in skill:
        if t == 1:
            degree = -degree
        tmp[r1][c1] += degree
        tmp[r1][c2+1]+= -degree
        tmp[r2+1][c1]+= -degree
        tmp[r2+1][c2+1] += degree
        
    for i in range(n):
        for j in range(m):
            tmp[i][j+1] +=tmp[i][j]
    
    for i in range(m):
        for j in range(n):
            tmp[j+1][i]+=tmp[j][i]
            board[j][i] += tmp[j][i]
            if board[j][i]>0:
                answer+=1
    return answer