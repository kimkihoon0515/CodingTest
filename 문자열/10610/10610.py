import sys

n = list(map(int,sys.stdin.readline().strip()))

if sum(n) % 3 == 0: # 3의 배수이면
    n = sorted(n,reverse=True) # 역순으로 정렬하고
    if n[-1] == 0: # 10의 배수이면
        print(''.join(map(str,n))) # n의 원소들을 문자열로 합친 후 출력
    else: # 그 외에는 전부 -1 출력
        print(-1) 

else:
    print(-1)
