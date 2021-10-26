import sys
from itertools import combinations
n = int(sys.stdin.readline()) # 추의 개수
w = list(map(int,sys.stdin.readline().split())) # 추들의 무게
m = int(sys.stdin.readline()) # 구슬의 개수
li = list(map(int,sys.stdin.readline().split())) # 구슬들의 무게
possible = []
ans = [[0 for _ in range(15001)] for _ in range(n+1)]

def scale(w,n,now,left,right):
    new = abs(left-right) # 왼쪽과 오른쪽 무게의 차 = 측정할 수 있는 무게
    if new not in possible: # possible에 없다면 그것을 추가한다.
        possible.append(new) 
    if now == n: # 추의 개수가 한계치에 다다르면 0으로 초기화.
        return 0
    if ans[now][new] == 0: # 측정할 수 있는 무게를 계산하는 반복문.
        scale(w,n,now+1,left+w[now],right) # 추의 개수를 하나 늘리고 왼쪽에 무게를 달아준다.
        scale(w,n,now+1,left,right+w[now]) # 추의 개수를 하나 늘리고 오른쪽에 무게를 달아준다.
        scale(w,n,now+1,left,right) 
        ans[now][new] = 1

scale(w,n,0,0,0)

for i in li:
    if i in possible:
        print('Y',end=' ')
    else:
        print('N',end=' ')