import sys
sdoku = []
for i in range(9):
    sdoku.append(list(map(int,sys.stdin.readline().split(' '))))

#빈칸(0) 개수 구하기
N = 0 # 빈칸 개수
for row in sdoku:
    N += row.count(0)
#print(N)

#빈칸들 인덱스 리스트 구하기
blanks=[]
for i in range(9):
    for j in range(9):
        if sdoku[i][j] ==0:
            blanks.append([i,j])
#print(blanks)

# 유망성 판단 함수 첫번째 인자는 빈칸의 위치(row,col) 두번째 인자는 i(1~9) / 특정 빈칸에 특정 값이 들어 가는 경우가 유망한지 판단
def promising(blank,i):
    if i in sdoku[blank[0]]:  #i 값이 같은 행에 이미 존재하면 탈락
         return False
    if i in [j[blank[1]] for j in sdoku]: #i 값이 같은 열에 존재하면 탈락
         return False

    # 해당 빈칸이 속한 3*3 행렬 추출
    square=[] # 해당 빈칸이 속한 3*3 행렬
    n= blank[0]//3
    m= blank[1]//3
    for j in range(3):
        for k in range(3):
            square.append(sdoku[3*n+j][3*m+k])

    if i in square: #i 값이 3*3 행렬에 존재하면 탈락
        return False

#백트랙킹 알고리즘 depth는 빈칸개수 각 깊이별 노드는 1~9
def dfs(cnt):
    if cnt == N: #N개 다 채우면 출력 후 종료
        for i in range(9):
            print(*sdoku[i])
        exit() # 모두 빈칸인 경우 하나의 스도쿠만 완성하고 코드를 종료하도록해야 채점 통과
        return

    for i in range(1,10):
        if promising(blanks[cnt],i) == False:
            continue

        else:
            sdoku[blanks[cnt][0]][blanks[cnt][1]] = i
            dfs(cnt+1)
            sdoku[blanks[cnt][0]][blanks[cnt][1]] = 0

dfs(0)