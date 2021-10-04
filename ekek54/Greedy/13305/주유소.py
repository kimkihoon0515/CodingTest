import sys
N= int(sys.stdin.readline())
dis = list(map(int,sys.stdin.readline().split(' ')))
oil = list(map(int,sys.stdin.readline().split(' ')))

for i in range(N-1):
    if oil[i]<oil[i+1]:
        oil[i+1]=oil[i]

res=0
for i in range(N-1):
    res+=dis[i]*oil[i]
print(res)
