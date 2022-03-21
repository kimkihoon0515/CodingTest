import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())

li = list(int(sys.stdin.readline().strip()) for _ in range(p))
parent = [i for i in range(g+1)] # 부모 리스트

def find(x): # 숫자에 해당하는 부모를 찾는 find 함수
    if parent[x] == x:
        return x
    parent[x] = find(parent[x])
    return parent[x]

ans = 0
for i in li:
    docking = find(i)
    if docking == 0:
        break
    parent[docking] = parent[docking-1]
    ans+=1
print(ans)