import sys

n,m = map(int,sys.stdin.readline().split())

hash = {}
cnt = 0

for _ in range(n):
    s = sys.stdin.readline().strip()
    hash[s] = True

word = list(sys.stdin.readline().strip() for _ in range(m))

for i in word:
    if i in hash.keys():
        cnt +=1
        
print(cnt)

