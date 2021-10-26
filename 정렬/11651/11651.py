n = int(input()) # n개만큼의 좌표를 입력받는다.

pos = [] # 좌표를 저장할 배열
for i in range(n): 
    x,y = map(int,input().split())
    pos.append([y,x])  # x,y를 바꿔서 저장하고 정렬한다.

pos.sort()

for i in range(len(pos)): # 출력할 때는 반대로 다시 바꿔서 출력한다.
    print(pos[i][1],pos[i][0])

  

