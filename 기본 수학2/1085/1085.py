x,y,w,h = map(int,input().split()) # x y w h 를 입력받는다.

x_distance = abs(x-w) # x축과의 거리의 절대값을 구한다.
y_distance = abs(y-h) # y축과의 거리의 절대값을 구한다.

min_x = 0 # x축상에서의 거리중 짧은 것
min_y = 0 # y축상에서의 거리중 짧은 것

if x_distance < x : # x축과의 거리중 짧은 것을 min 값으로 둔다.
    min_x = x_distance
else:
    min_x = x
if y_distance < y : # y축과의 거리중 짧은 것을 min 값으로 둔다.
    min_y = y_distance
else:
    min_y = y
if min_x < min_y:
    print(min_x)
else:
    print(min_y)