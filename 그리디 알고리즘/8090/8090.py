import sys

n,c = map(int,sys.stdin.readline().split()) # 마을 수,트럭의용량
m = int(sys.stdin.readline()) # 박스개수

box = []
for _ in range(m):
    box.append(list(map(int,sys.stdin.readline().split()))) # 출발지,도착지,박스개수
    
box.sort(key=lambda x:x[1]) # 도착지를 기준으로 정렬한다.
#print(box)

truck = [c for _ in range(n+1)]
ans = 0
for i,j,k in box: # i:출발지,j:도착지,k:박스개수
    MIN = c # 최소값
    for l in range(i,j): # i번째에서 출발지와 도착지 범위중에 
        MIN = min(MIN,truck[l]) # 마을의 최소값과 박스 중 가장 적은 것을 고른다.
    MIN = min(MIN,k) 
    
    for m in range(i,j):
        truck[m] -= MIN # 마을 수용 박스 수에서 MIN 값을빼주고
    ans += MIN # 결과값에는 트럭에서 내린 박스 양을 더해준다.
    
print(ans)