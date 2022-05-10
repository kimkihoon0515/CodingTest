# 풀이 참고함. 나중에 다시 풀어볼 것.

import sys
from collections import deque

def right(a,b):
    if a>4 or graph[a-1][2] == graph[a][6]:
        return
    if graph[a-1][2]!=graph[a][6]:
        right(a+1,-b)
        graph[a].rotate(b)
        
def left(a,b):
    if a<1 or graph[a][2]   == graph[a+1][6]:
        return
    if graph[a+1][6]!=graph[a][2]:
        left(a-1,-b)
        graph[a].rotate(b)

graph = {}

for i in range(1,5):
    graph[i] = deque(list(map(int,list(sys.stdin.readline().replace('\n',"")))))

n = int(sys.stdin.readline())

for _ in range(n):
    a,b = map(int,sys.stdin.readline().split())
    right(a+1,-b)
    left(a-1,-b)
    graph[a].rotate(b)
    
answer = 0
for i in range(4):
    answer += (2**i)*graph[i+1][0]

print(answer)