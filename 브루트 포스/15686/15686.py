import sys
from itertools import combinations

n,m = map(int,sys.stdin.readline().split())

li = []

for _ in range(n):
    li.append(list(map(int,sys.stdin.readline().split())))

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if li[i][j] == 1:
            home.append((i,j))
        elif li[i][j] == 2:
            chicken.append((i,j))

com = list(combinations(chicken,m))
#print(com)
result = [0 for _ in range(len(com))]
#print(home)
#print(chicken)

for i in home:
    for j in range(len(com)):
        min_length = sys.maxsize 
        for k in com[j]: 
            length = abs(i[0]-k[0])+abs(i[1]-k[1]) # 치킨 거리를 구하는 식
            min_length = min(min_length,length) # 치킨 거리의 최소값을 구하고
        result[j] += min_length # 도시 치킨거리를 구하는 식
print(min(result)) # 도시 치킨 거리가 최소가 되는 것 출력