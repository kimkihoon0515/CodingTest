import sys

t = int(sys.stdin.readline())   

for _ in range(t):
    n,m = map(int,sys.stdin.readline().split())
    a= sorted(list(map(int,sys.stdin.readline().split())))
    b = sorted(list(map(int,sys.stdin.readline().split())))
    cnt =0
    for i in a:
        left = 0 # 시작점
        right = m-1 # 끝점
        answer = -1 # 최대값비교를 위해서 -1로 설정
        while left <= right:
            mid = (left+right)//2 # 중간 지점
            if i >b[mid]: # a의 원소가 b의 원소보다 크면
                left = mid +1
                answer = max(mid,answer)
            else: # a의 원소가 b의 원소보다 작으면
                right = mid -1
        cnt += answer + 1 # a가 b보다 큰 순서쌍의 개수를 하나씩 늘려간다.
    print(cnt)
        