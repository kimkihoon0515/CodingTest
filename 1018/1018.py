n,m = map(int,input().split()) # n,m을 입력받는다.

board = [list(map(str,input())) for _ in range(n)] # 보드를 2차원배열로 입력받는다.
 
count_arry=[] # cnt와 count를 담을 배열을 선언한다.
for a in range(n-7): 
    for b in range(m-7):
        cnt=0
        count = 0
        for i in range(a,a+8): # 자르는범위의 시작점
            for j in range(b,b+8): #자르는 범위의 시작점
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