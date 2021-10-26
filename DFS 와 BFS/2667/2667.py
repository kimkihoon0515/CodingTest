import sys

n = int(sys.stdin.readline())

li = []

dx = [0,0,1,-1] # x방향으로 오른쪽,왼쪽
dy = [1,-1,0,0] # y방향으로 오른쪽,왼쪽

cnt = 0 # 단지 내 집의 수를 저장하는 변수
count = 0 # 총 단지의 수를 저장하는 변수

def dfs(x,y):
    global cnt 
    if x < 0 or x >= n or y <0 or y>=n: # x,y 가 범위를 벗어나면 false
        return False
    if li[x][y] ==1: # 배열에 집이 있다면 
        cnt +=1 # 집의 수를 하나씩 늘려가고 그곳은 탐색한 곳이므로 0으로 만들어준다.
        li[x][y] = 0
        for i in range(4): # x,y 를 움직이는 경우의 수 
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx,ny) # 재귀 호출
        return True
    return False        


for i in range(n):
    li.append(list(map(int,input())))

result = []
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            count +=1 # 단지가 총 몇개인지 구하기 위해 True를 반환할 때마다 하나씩 늘려준다. 
            result.append(cnt) # 집의 개수를 배열에 넣고 sort해준다.
            cnt = 0
print(count)
result.sort()
for i in range(len(result)):
    print(result[i])

