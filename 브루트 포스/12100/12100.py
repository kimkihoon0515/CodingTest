import sys
from copy import deepcopy

n = int(sys.stdin.readline())

li = []
for _ in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))

def up(li):
    for i in range(n):
        a = 0 # 행의 가장 윗부분
        x  = 0 # 블록 합쳐지는것
        for j in range(n):
            if li[j][i] == 0: 
                continue
            if x == 0: # 더할 블록이 없으므로 
                x = li[j][i] # x를 변경
            else:
                if x == li[j][i]: # 지난블록이랑 같으면 ex) 4 4
                    li[a][i] = x * 2 # 이동할 곳에 합쳐서 놓는다.
                    x = 0 # 블록 더했으므로 0으로 초기화
                    a += 1 # 가장 위쪽 행을 채웠으므로 다음 블록이 이동하게 될 위치 증가
                else: # 지난블록이랑 같지 않을경우
                    li[a][i] = x # 이동할 위치에 지난 블록 x 저장
                    x = li[j][i] # x에 새로운 블록으로 변경
                    a += 1 # 하나 더 증가
            li[j][i] = 0 # 블록 이동했으므로 비운다.
        if x !=0: #
            li[a][i] = x
    return li

def down(li):
    for i in range(n):
        a = n-1 # 행의 가장 아래쪽
        x = 0
        for j in range(n-1,-1,-1):
            if li[j][i] == 0:
                continue
            if x == 0:
                x = li[j][i]
            
            else:
                if x == li[j][i]:
                    li[a][i] = x * 2
                    x = 0
                    a -= 1
                else:
                    li[a][i] = x
                    x = li[j][i]
                    a -=1
            li[j][i] = 0
        if x !=0:
            li[a][i] = x
    return li

def right(li):
    for i in range(n):
        a = n-1 # 열의 가장 오른쪽
        x = 0
        for j in range(n-1,-1,-1):
            if li[i][j] == 0:
                continue
            if x == 0:
                x = li[i][j]
            else:
                if x == li[i][j]:
                    li[i][a] = x * 2
                    x = 0
                    a -= 1
                else:
                    li[i][a] = x
                    x = li[i][j]
                    a -=1
            li[i][j] = 0
        if x !=0:
            li[i][a] = x
    return li

def left(li):
    for i in range(n):
        a = 0 # 열의 가장 왼쪽
        x = 0
        for j in range(n):
            if li[i][j] == 0:
                continue
            if x == 0:
                x = li[i][j]
            else:
                if x == li[i][j]:
                    li[i][a] = x * 2
                    x = 0
                    a += 1

                else:
                    li[i][a] = x
                    x = li[i][j]
                    a += 1

            li[i][j] = 0
        if x !=0:
            li[i][a] = x
    return li

def solve(li,cnt):
    global result
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                result = max(result,li[i][j])
        return
    
    solve(left(deepcopy(li)),cnt+1)
    solve(right(deepcopy(li)),cnt+1)
    solve(up(deepcopy(li)),cnt+1)
    solve(down(deepcopy(li)),cnt+1)

result = 0
solve(li,0)
print(result)