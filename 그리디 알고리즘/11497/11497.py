import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    li = sorted(list(map(int,sys.stdin.readline().split())))
    answer = 0
    for i in range(2,n):
        answer = max(answer,li[i]-li[i-2]) # 인덱스 2차이나는 값이 가장 적게끔 만든다.
    print(answer)