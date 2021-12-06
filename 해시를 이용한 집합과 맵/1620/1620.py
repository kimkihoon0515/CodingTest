import sys

n,m = map(int,sys.stdin.readline().split())


hash = {}
hash1= {}

poke = [sys.stdin.readline().strip() for _ in range(n)]
for i in range(len(poke)):
    hash[poke[i]] = hash.get(poke[i],i+1)
    hash1[i+1] = hash1.get(i+1,poke[i])

for _ in range(m):
    ans = sys.stdin.readline().strip()
    if ans.isdigit(): # 입력값이 정수면
        print(hash1[int(ans)]) # 정수로 된 key에서 value값을 출력
    else: # 그렇지 않으면
        print(hash[ans]) # str로 된 key에서 value 값 출력 
    