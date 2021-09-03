import sys
N, M=map(int,sys.stdin.readline().split(' '))
numlist=[i+1 for i in range(N)] #
checklist=[False]*N #사용안함
result=[]
def dfs(cnt): #깊이 우선 탐색
    if cnt==M: # 최대 깊이 도달
        print(*result) # 출력 후 종료
        return
    for i in range(N): # sibling 노드 탐색 loop
        result.append(numlist[i])
        dfs(cnt+1) # child로 이동
        result.pop() # 전 상태로 돌아가기

dfs(0)