import sys


n,m = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))
li.sort() # 오름차순 정렬
answer = []

def dfs(index): 
    if index == m: # m 번 돌린 후에
        print(' '.join(map(str,answer))) # answer배열을 출력한다. 
        return
    for i in range(n):
        if not answer or answer[-1] <= li[i]: # 만약 answer의 마지막값이 li[i] 이하이면
            answer.append(li[i]) # answer배열에 li[i]를 넣어주고 
            dfs(index+1) # dfs의 횟수를 1증가시킨다.
            answer.pop()

dfs(0)
