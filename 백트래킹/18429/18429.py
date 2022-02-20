import sys
from itertools import permutations

n,k = map(int,sys.stdin.readline().split())

a = list(map(int,sys.stdin.readline().split()))

ans = 0
for i in permutations(a,n): # 모든 경우의 수를 계산해놓음 
    weight = 500
    for j in i:
        weight = weight +j-k # 각 일차가 지난 후 몸무게
        if weight <500: # 만약 무게가 500보다작으면
            break
    else: # 그렇지 않다면 답의 개수를 1개 증가시킨다.
        ans += 1
        
print(ans)