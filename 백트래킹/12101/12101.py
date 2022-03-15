import sys

n,k = map(int,sys.stdin.readline().split())

num = [1,2,3]

def solution(sum,ans):
    global cnt
    if sum > n:
        return 
    if n == sum:
        cnt +=1
        if cnt == k:
            print(ans[:-1])
            exit()
    for i in num:
        solution(sum+i,ans+str(i)+'+')
cnt = 0
solution(0,'')
print(-1)
