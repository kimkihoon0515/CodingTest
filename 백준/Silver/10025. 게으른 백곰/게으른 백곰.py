import sys

n,k = map(int,sys.stdin.readline().split())

li = [0 for i in range(1000001)]
end = 0
for _ in range(n):
    g,x = map(int,sys.stdin.readline().split())
    li[x] = g
    end = max(end,x)
    
step = 2*k+1
window = sum(li[:step])
answer = window

for i in range(step,end+1):
    window += li[i] - li[i-step]
    answer = max(answer,window)
print(answer)