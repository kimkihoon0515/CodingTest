x,y,w,h = map(int,input().split()) # x y w h 를 입력받는다.

x_distance = abs(x-w)
y_distance = abs(y-h)

min_x = 0
min_y = 0

if x_distance < x :
    min_x = x_distance
else:
    min_x = x
if y_distance < y :
    min_y = y_distance
else:
    min_y = y
if min_x < min_y:
    print(min_x)
else:
    print(min_y)