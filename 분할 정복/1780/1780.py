import sys

n = int(sys.stdin.readline())

li = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
a=0
b=0
c=0
def cut(x,y,n):
    global a,b,c
    check = li[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check !=li[i][j]:
                cut(x,y,n//3)
                cut(x,y+n//3,n//3)
                cut(x,y+2*n//3,n//3)
                cut(x+n//3,y,n//3)
                cut(x+n//3,y+n//3,n//3)
                cut(x+n//3,y+2*n//3,n//3)
                cut(x+2*n//3,y,n//3)
                cut(x+2*n//3,y+n//3,n//3)  
                cut(x+2*n//3,y+2*n//3,n//3)
                return
    if check == -1:
        a +=1
        return
    elif check == 0:
        b +=1
        return
    else:
        c +=1
        return
cut(0,0,n) 
print(a)
print(b)
print(c)

