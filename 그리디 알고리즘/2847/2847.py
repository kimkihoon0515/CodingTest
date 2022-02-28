import sys

n = int(sys.stdin.readline())

score = [int(sys.stdin.readline().strip()) for _ in range(n)]

cnt = 0
for i in range(n-1,0,-1):
    if score[i] <= score[i-1]: # 앞의 문제보다 뒤의 문제가 더 작으면
       cnt += (score[i-1] - score[i]+1) # 차이 + 1 만큼 더해줘서 앞의 숫자가 뒤의 숫자보다 작게 한다.
       score[i-1] = score[i] - 1 # score 갱신
print(cnt) 