n,s = map(int,input().split()) # 합이 s가 되는 수열의 갯수를 구해라. 숫자는 n개만큼 입력받는다.

list=list(map(int,input().split()))

cnt = 0
def dfs(i,sum):
    global cnt
    if i >=n:
        return
    sum += list[i]
    if sum == s:
        cnt +=1
    dfs(i+1,sum-list[i])
    dfs(i+1,sum)

dfs(0,0)
print(cnt)
