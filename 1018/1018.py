n,m = map(int,input().split())

board = [list(map(str,input())) for _ in range(n)]

count_arry=[]
for a in range(n-7):
    for b in range(m-7):
        cnt=0
        count = 0
        for i in range(a,a+8):
            for j in range(b,b+8):
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        cnt +=1
                    if board[i][j] != 'B':
                        count +=1
                else:
                    if board[i][j] != 'B':
                        cnt+=1
                    if board[i][j] != 'W':
                        count+=1
        count_arry.append(min(cnt,count))
print(min(count_arry))