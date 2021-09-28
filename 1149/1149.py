n = int(input()) # 집의 수를 입력받는다.

li = [] # 각각의 집의 색의 가격을 넣는 배열

for i in range(n):
    li.append(list(map(int,input().split())))


for i in range(1,len(li)): 
    li[i][0] = min(li[i-1][1],li[i-1][2])+li[i][0] # i번째 집이 빨간색일 때 최소값
    li[i][1] = min(li[i-1][0],li[i-1][2])+li[i][1] # i번째 집이 파란색일 때 최소값
    li[i][2] = min(li[i-1][0],li[i-1][1])+li[i][2] # i번째 집이 노란색일 때 최소값
print(min(li[n-1][0],li[n-1][1],li[n-1][2])) # 그것들 중 최소값을 구함.