import sys

n,s = map(int,sys.stdin.readline().split())

li = list(map(int,sys.stdin.readline().split()))

left = 0
right = 0
sum = 0
minimum = sys.maxsize # 합이 s를 넘어서는 최소값을 구하는 변수

while True:
    if sum >=s: # 합이 s를 넘어서면 왼쪽 지점을 하나 없애고 합에서 그것을 뺀다.
        sum -=li[left]
        left +=1
        minimum = min(minimum,right-left+1) # 길이의 최소값을 구하는 것
    else:
        if right == n: # 만약 배열의 길이와 오른쪽 끝이 같아지면 종료한다.
            break
        else: # 합이 s를 넘어서지도 못하고 오른쪽 끝부분이 배열의 길이와 같지 않으면
            sum +=li[right] # 오른쪽을 하나증가시키고 합을 늘려준다.
            right +=1

if minimum == sys.maxsize: # 모든 합이 s를 넘지 못하면 그것을 만족하는 길이는 0
    minimum = 0
print(minimum)