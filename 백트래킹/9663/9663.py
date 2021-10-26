n = int(input()) # 보드의 수를 n개로 정한다.

board = [0] * 15 # 보드의 최대 개수를 정해놓는다.
 
def possible(x): # 퀸이 존재할 수 있는 조건
    for i in range(x):
        if board[i] == board[x] or abs(board[i]-board[x]) == x-i:
            return False
    return True

result = 0
def dfs(x): # 검사하는 dfs 알고리즘
    global result
    if x == n:
        result +=1
    else:
        for i in range(n):
            board[x] = i
            if possible(x):
                dfs(x+1)  
dfs(0)                
print(result)