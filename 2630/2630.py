import sys

n = int(sys.stdin.readline())

li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] # 타일의 색깔을 입력받는다.

white = 0 
blue = 0
def cut(x,y,n):
    global blue,white 
    check = li[x][y] # 가장 처음 0,0 번째 타일의 색을 지정하고 반복문을 돌려서 하나씩 증가시켜서 색이 다르면 4등분하고 다시 돌린다.
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check != li[i][j]:
                cut(x,y,n//2) # 1사분면
                cut(x,y+n//2,n//2) # 2사분면
                cut(x+n//2,y,n//2) # 3사분면
                cut(x+n//2,y+n//2,n//2) # 4사분면
                return 
    if check ==0: # 모든 색이 흰색
        white +=1
        return
    else: # 모든 색이 파란색
        blue +=1

        return
cut(0,0,n)
print(white)
print(blue)