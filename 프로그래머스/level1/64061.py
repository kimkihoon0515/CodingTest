def solution(board, moves):
    answer = 0
    
    queue = []
    
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] !=0:
                queue.append(board[j][i-1])
                board[j][i-1] = 0
                
                if len(queue)>1:
                    for j in range(1,len(queue)):
                        if queue[j] == queue[j-1]:
                            queue.pop(-1)
                            queue.pop(-1)
                            answer+=2
                break
    return answer