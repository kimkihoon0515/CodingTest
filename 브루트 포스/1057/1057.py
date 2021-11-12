import sys

n,k,l = map(int,sys.stdin.readline().split())

round = 0

while k != l: # 토너먼트의 규칙 사용
    k -= k // 2
    l -= l // 2
    round +=1
print(round)