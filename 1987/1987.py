r,c = map(int,input().split()) # 세로 R칸 가로 C칸으로 된 보드

arr = [list(map(str,input())) for _ in range(r)] # 조건에 따라 입력받은 보드의 알파벳

result = []

dx = [0,0,1,-1] # 좌 하 우 상
dy = [1,-1,0,0]
answer = 1
def move(x,y,index):
    global answer

    answer = max(index,answer)
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0<= nx <r and 0<= ny <c) and arr[x][y] not in result:
            print(arr[nx][ny])
            result.append(arr[nx][ny])
            print(result)
            move(nx,ny,index+1)
            result.pop()
            
move(0,0,answer)
print(answer)

