import sys

s = list(map(str,input()))

column = int(ord(s[0])-int(ord('a'))+1) # 가로
row = int(s[1]) # 세로

dx = [2,-2,2,-2,1,-1,1,-1]
dy = [1,1,-1,-1,2,2,-2,-2]

cnt = 0
for i in range(8):
    nx = column + dx[i]
    ny = row + dy[i]
    
    if 0 < nx <= 8 and 0 < ny <= 8:
        cnt +=1
print(cnt)