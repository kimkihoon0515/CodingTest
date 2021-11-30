import sys


n = int(sys.stdin.readline()) # 고속도로에 N개의 센서 설치 최대 K개의 집중국 세우기 가능.
k = int(sys.stdin.readline())
s = sorted(list(map(int,sys.stdin.readline().split())))

if k >= n: # 최대 개수가 센서 수보다 많으면 0을 출력하고 종료
    print(0)
    exit(0)

dist = [] # 거리 배열
for i in range(1,n):
    dist.append(s[i]-s[i-1]) # 두 센서 사이의 거리를 배열에 넣는다.
dist = list(sorted(dist)) # 거리순으로 정렬
for i in range(k-1): # k-1만큼 빼준다.
    dist.pop()
sum = 0
for i in dist: # 총합을 구해줘서 출력한다.
    sum += i
print(sum)