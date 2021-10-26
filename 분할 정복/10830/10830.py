import sys
n,b=map(int,sys.stdin.readline().split())
a=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]
 
 
def mul(a,b):
    tmj=[[0 for _ in range(n)] for _ in range(n)]
    if b==1:
        for i in range(n):
            for j in range(n):
                a[i][j]%=1000
        return a
 
    elif b%2==1:
        c=mul(a,b-1)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmj[i][j]+=c[i][k]*a[k][j]
                tmj[i][j]%=1000
 
        return tmj
 
    else:
        c=mul(a,b//2)
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmj[i][j]+=c[i][k]*c[k][j]
                tmj[i][j]%=1000
        return tmj
 
result=mul(a,b)
for li in result:
    for j in li:
        print(j,end=' ')
    print()
