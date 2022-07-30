import sys

n,m = map(int,sys.stdin.readline().split())

board = [list(map(str,sys.stdin.readline().strip())) for _ in range(n)]

cnt = 0
for i in range(n):
    start = ''
    for j in range(m):
        if board[i][j]=='-' and board[i][j]!=start:
            cnt +=1
        start = board[i][j]

cnt1 = 0
for i in range(m):
    start1 = ''
    for j in range(n):
        if board[j][i] == '|' and board[j][i]!=start1:
            cnt1+=1
        start1 = board[j][i]

print(cnt+cnt1)