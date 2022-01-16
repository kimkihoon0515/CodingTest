import sys

n,m = map(int,sys.stdin.readline().split())
if n == 1:
    print(1)
elif n == 2: # 세로가 2이면 2,3 2가지 방법밖에 쓸 수 없으므로
    print(min(4,(m-1)//2+1)) # 가로의 길이에 상관없이 최대 4번움직일 수 있다. 
elif m <= 6: # 가로의 길이가 6 이하인경우
    print(min(4,m)) # 4번이상 움직이면 모든 방법을 다 써야하므로 최대 4 이고 최소값은 가로의 길이
else:
    print(m-2) # 그 외의 경우에는 오른쪽으로 2 칸 가는 방법빼고 한 칸씩만 이동