def solution(n):
    answer = [[0 for j in range(i+1)] for i in range(n)]
    dx=[0,1,-1] 
    dy=[1,0,-1] # 
    direction=0
    cur=[0,0]
    idx=1
    answer[cur[0]][cur[1]]=idx
    idx+=1
    cnt=0
    while cnt<3: 
        nx=cur[1]+dx[direction%3]
        ny=cur[0]+dy[direction%3]
        if ny<0 or n<=ny or nx<0 or len(answer[ny]) <= nx:#벽에 부딪히면 방향전환
            direction+=1
            cnt+=1
            continue
        if answer[ny][nx]!=0: # 방문한 노드이면 방향전환
            direction+=1
            cnt+=1
            continue
        cur[0]=ny
        cur[1]=nx
        answer[cur[0]][cur[1]]=idx
        idx+=1
        cnt=0

    return [j for i in answer for j in i]