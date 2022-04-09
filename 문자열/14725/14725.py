import sys

n = int(sys.stdin.readline())

food = []

for _ in range(n):
    information = list(sys.stdin.readline().split()) # 먹이 개수, 먹이 정보
    food.append(information[1:]) # 먹이 정보만 배열에 넣기

food.sort() # 알파벳 순으로 정렬

ans = []
for i in range(n):
    if i == 0:
        for j in range(len(food[i])):
            ans.append('--'*j+food[i][j])
    else:
        index = 0
        for j in range(len(food[i])):
            if food[i-1][j] != food[i][j] or len(food[i-1]) <=j:
                break
            else:
                index = j+1
        for j in range(index,len(food[i])):
            ans.append('--'*j+food[i][j])

for i in ans:
    print(i)

