import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))
answer = 0

def dfs(s):
    global answer
    
    if len(li) == 2:
        if s > answer:
            answer = s
        return
    else:
        for i in range(1,len(li)-1):
            energy = li[i-1]*li[i+1]
            x = li[i]
            del li[i]
            dfs(s+energy)
            li.insert(i,x)
            
dfs(0)
print(answer)