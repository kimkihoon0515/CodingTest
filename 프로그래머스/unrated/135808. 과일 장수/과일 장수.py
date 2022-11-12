def solution(k, m, score):

    score = sorted(score,reverse=True)

    res = [score[i:i+m] for i in range(0,len(score), m)]
    
    result = []
    for i in res : 
        if len(i) == m: 
            result.append(min(i) * m) 
    ans = sum(result)
    return ans 