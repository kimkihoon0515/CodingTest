A, B, C = map(int,input().split()) # 3개의 숫자를 입력받는다.

if B>=C: # 어떤 경우에도 손익분기점을 못 넘을 경우에는
    print(-1) # -1을 출력하고
else: # 그 경우가 아니면
    print(int(A/(C-B)+1)) # 손익분기점을 넘는 답을 구한다.