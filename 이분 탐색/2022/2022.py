import sys,math

x,y,c = map(float,sys.stdin.readline().split())

left = 0
right = min(x,y)

while abs(left-right)>1e-6:
    mid = (left+right) / 2.0
    d = mid
    h1 = math.sqrt(x**2-d**2) # x 사다리 기준 높이
    h2 = math.sqrt(y**2-d**2) # y 사다리 기준 높이
    h = h1*h2 / (h1+h2) # c와 비교할 높이 
    if h > c:
        left = mid
    else:
        right = mid
print('%.3f'%round(mid,3))