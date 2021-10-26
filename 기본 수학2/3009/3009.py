x_points=[] # x축의 배열을 만든다.
y_points=[] # y축의 배열을 만든다.

for i in range (3): # 3개만큼의 x,y를 입력받고 각각의 배열에 넣는다.
    x,y = map(int,input().split())
    x_points.append(x)
    y_points.append(y)

x_cnt = 0 # x 의 좌표 종류의 개수를 받는 변수
y_cnt = 0 # y 의 좌표 종류의 개수를 받는 변수
x_ans=0 
y_ans=0

for i in range(3):
    if x_points.count(x_points[i]) == 1: # x 좌표의 종류의 개수가 1이면 출력
        x_ans=x_points[i]
    if y_points.count(y_points[i]) == 1: # y 좌표의 종류의 개수가 1이면 출력
        y_ans=y_points[i]
print(x_ans,y_ans)