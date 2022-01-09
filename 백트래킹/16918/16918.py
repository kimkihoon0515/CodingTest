import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))
answer = 0

def dfs(s):
    global answer
    
    if len(li) == 2: # 구슬 수가 2개가 되면 종료
        if s > answer:
            answer = s
        return
    else: 
        for i in range(1,len(li)-1): 
            energy = li[i-1]*li[i+1] # 에너지 정의
            x = li[i] 
            del x # 선택한 구슬을 빼서 재귀를 돌린다.
            dfs(s+energy)
            li.insert(i,x) # 빼기 전 구슬을 다시 넣는다.
            
dfs(0)
print(answer)