import sys
N=int(sys.stdin.readline())
rowlist=[0]*N #결과를 갖는 배열로 각 col에 대한 row 값들이 들어간다. col:인덱스 값임으로 0~(N-1) / row: 1~N 으로 표현(배열을 0으로 초기화해서)
result= 0
def promising(depth,node): # depth 값의 깊이에서 입력받는 행(노드)에 퀸을 두는것에 대한 유망성 검사 함수
    if depth==0: # 체스판에 아무것도 놓여있지 않은 경우
        return True
    for i in range(depth):
        if rowlist[i] == node: #같은 행에 존재하는 경우 탈락
            return False
        elif abs(depth-i)==abs(rowlist[i]-node): #대각선에 있는 경우 탈락(col의 차이와 row의 차이가 같으면 대각선에 존재)
            return False
def dfs(cnt): #깊이 우선 탐색
    global result # 결과값 전역변수 선언
    if cnt==N: # 최대 깊이 도달
        #print(*rowlist) # 출력 후 종료
        result= result+1
        return
    for i in range(1,N+1): # sibling 노드 탐색 loop
        if promising(cnt,i) == False: #유망하지 않은 경우
            continue
        else: #유망한 경우
            rowlist[cnt]=i #유망한 행 넣기
            dfs(cnt+1) #다음 깊이 탐색
            rowlist[cnt]=0 # 전상태로 되돌리기
dfs(0)
print(result)