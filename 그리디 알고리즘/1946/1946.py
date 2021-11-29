import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    li = []
    for _ in range(n):
        score,rank = map(int,sys.stdin.readline().split())
        li.append([score,rank])
    li.sort() # 서류심사 순으로 정렬
    maximum = li[0][1] # 면접 순위 비교를 위해
    cnt = 1 # 서류 심사 1등은 바로 합격이므로
    for i in range(1,n):
        if maximum > li[i][1]: # 면접 순위가 크면 i번째 지원자는 면접 순위로는 이기게 되므로 합격이 된다.
           cnt += 1 
           maximum = li[i][1] # 면접 순위중 가장 높은 순위를 마지막 합격한 순위로 바꾼다
    print(cnt) 