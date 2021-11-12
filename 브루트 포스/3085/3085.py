import sys

n = int(sys.stdin.readline())

li = [list(map(str,input())) for _ in range(n)]

def check(li):
    global n
    answer = 1 # 사탕의 개수
    for i in range(n):
        cnt = 1 
        for j in range(1,n):
            if li[i][j] == li[i][j-1]: # 가로로 인접한 사탕이 같으면
                cnt +=1 # cnt 1증가
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt # 먹을 수 있는 사탕의 최대 개수에 저장
        cnt = 1
        for j in range(1,n): 
            if li[j][i] == li[j-1][i]: # 세로로 인접한 사탕이 같으면
                cnt +=1 # cnt 1증가
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt # 먹을 수 있는 사탕의 최대 개수에 저장
    return answer

result = 0

for i in range(n):
    for j in range(n):
        if j < n-1: # 가로로 교환
            li[i][j],li[i][j+1] = li[i][j+1],li[i][j]
            if check(li) > result:
                result = check(li)
            li[i][j],li[i][j+1] = li[i][j+1],li[i][j] # 되돌려놓기
        if i < n -1: # 세로로 교환
            li[i][j],li[i+1][j] = li[i+1][j],li[i][j]
            if check(li) > result:
                result = check(li)
            li[i][j],li[i+1][j] = li[i+1][j],li[i][j] # 되돌려놓기

print(result)