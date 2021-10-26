n = int(input())

pos = [] # 좌표를 입력받는다.
for _ in range(n):
    x,y = list(map(int,input().split()))
    pos.append([x,y]) # 좌표에 x,y를 각각 대입하고
 
pos.sort() # 정렬하고 출력한다.
for i in range(len(pos)):
    print(pos[i][0],pos[i][1])


