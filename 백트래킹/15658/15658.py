import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

plus,minus,mul,div = map(int,sys.stdin.readline().split())

minimum = sys.maxsize
maximum = -sys.maxsize

def dfs(i,ans,plus,minus,mul,div):
    global minimum,maximum
    
    if i == n: # 숫자 수와 연산횟수가 같아지면 결과값 출력
        minimum = min(ans,minimum)
        maximum = max(ans,maximum)
        return
    if plus > 0:
        dfs(i+1,ans+li[i],plus-1,minus,mul,div)
    if minus > 0:
        dfs(i+1,ans-li[i],plus,minus-1,mul,div)
    if mul > 0:
        dfs(i+1,ans*li[i],plus,minus,mul-1,div)
    if div > 0:
        dfs(i+1,int(ans/li[i]),plus,minus,mul,div-1)

dfs(1,li[0],plus,minus,mul,div)
print(maximum)
print(minimum)
        
        