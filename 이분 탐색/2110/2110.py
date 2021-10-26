import sys

n,c = map(int,sys.stdin.readline().split())

li = []

for i in range(n):
    li.append(int(sys.stdin.readline()))

li.sort()
start = 1
end = li[-1]
result = 0

while start <= end:
    mid = (start + end) //2
    cnt = 1 
    old = li[0] # 공유기 설치된 집
    for i in li:
        if i >=old+mid: # 사이간격보다 더 멀다면 old를 갱신한다.
            cnt+=1
            old = i
    if cnt >=c:
        start = mid+1
    else:
        end = mid-1
print(end)

