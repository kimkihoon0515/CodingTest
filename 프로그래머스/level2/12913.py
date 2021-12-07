def solution(land):
    for i in range(1,len(land)):
        for j in range(len(land[0])): 
            land[i][j] += max(land[i-1][:j]+land[i-1][j+1:]) # 조건에 맞게 최대값을 계속 더해간다
    return max(land[-1])