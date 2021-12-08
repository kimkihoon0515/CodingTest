import sys

n = int(sys.stdin.readline())

m = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().split()))

cnt = 0
sum = 0

for start in range(n):
    end = start+1 # end는 무조건 시작점에서 1 증가한 것에서부터 출발 -> 안그러면 시작지점*2 가 m일 경우도 세어짐
    while end < n:
        sum = li[start] + li[end] 
        end +=1
        if sum == m: # 조건에 맞으면 
            cnt +=1 # 개수 1 증가
print(cnt)     