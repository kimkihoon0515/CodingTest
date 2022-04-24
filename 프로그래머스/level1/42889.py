def solution(N, stages):
    answer = []
    result = {}
    players = len(stages)
    
    for i in range(1,N+1):
        if players!=0:
            cnt = stages.count(i)
            result[i] = cnt/players
            players-=cnt
        else:
            result[i] = 0
    result = sorted(result,key=lambda x:result[x],reverse=True)
    return result